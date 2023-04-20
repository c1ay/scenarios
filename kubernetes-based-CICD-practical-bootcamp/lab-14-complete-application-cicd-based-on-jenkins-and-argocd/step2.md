## Development Pipeline

We have already developed multi-branch version auto-publishing in our previous experiments, today's experiment we modify on this basis, first look at the original pipeline code, as follows:

```groovy
def call(params){

def tools = new org.devops.tools()

pipeline {
  agent {
        kubernetes {
            label "jenkins-slave-${UUUID.randomUUUID().toString()}"
            yaml """
apiVersion: v1
kind: Pod
spec.
  containers.
  - name: golang
    image: registry.cn-hangzhou.aliyuncs.com/coolops/golang:1.18.5
    command: ['cat']
    tty: true
  - name: docker
    image: registry.cn-hangzhou.aliyuncs.com/coolops/docker:19.03.11
    command: ['cat']
    tty: true
    volumeMounts.
      - name: indocker
        mountPath: /var/run/docker.sock
  - name: helm
    image: registry.cn-hangzhou.aliyuncs.com/coolops/helm-kubectl:3.2.4
    command: ['cat']
    tty: true
    volumeMounts.
      - name: kubeconfig
        mountPath: /root/.kube
  volumes.
    - name: indocker
      hostPath.
        path: "/var/run/docker.sock"
    - name: kubeconfig
      hostPath.
        path: "/home/shiyanlou/.kube"
"""
        }
    }

    environment{
        APP_NAME = "${params.APP_NAME}"
        INGRESS_HOST_PRE = "${params.INGRESS_HOST_PRE}"
        INGRESS_ENABLE = "${params.INGRESS_ENABLE? params.INGRESS_ENABLE :false}"
        IMAGE_REPO = ""
        IMAGE_TAG = ""
        HELM_COMMON_ARGS= "--set ingress.enabled=$INGRESS_ENABLE \
                           --set containers.port=8080 \
                           --set containers.healthCheak.path=/health \
                           --set ingress.hosts[0].paths[0].path=/ \
                           --set ingress.hosts[0].paths[0].pathType=ImplementationSpecific deploy/charts/ "
    }

    triggers {
        GenericTrigger(
        genericVariables: [
        [key: 'ref', value: '$.ref']
        ].
        causeString: 'Triggered on $ref'.
        token: 'go-hello-world'.
        printContributedVariables: true.
        printPostContent: true.
        silentResponse: false.
        regexpFilterText: '$ref'.
        regexpFilterExpression: 'refs/heads/(dev|test|uat|pre|prod)'
        )
    }

    stages {
        stage('Get Code') {
            steps {
                checkout(scm)
            }
        }

        stage('Get Image Repo') {
            steps {
                script{
                    BRANCH = ref - "refs/heads/"
                    IMAGE_REPO = "10.111.127.141:30002/${BRANCH}/${APP_NAME}"
                }
            }
        }

        stage('Build Code') {
            steps {
                container('golang'){
                    script{
                        sh '''
                            export GOPROXY=https://goproxy.cn
                            export GOOS=linux
                            export GOARCH=386
                            go mod tidy
                            go build -v -o . /${APP_NAME}
                        '''
                    }
                }
            }
        }
        stage('Build And Push Image') {
            steps {
                container('docker'){
                    script{

                        IMAGE_TAG = tools.createImageTag()
                        sh """
                            docker login 10.111.127.141:30002 -u admin -p Harbor12345
                            docker build -t ${IMAGE_REPO}:${IMAGE_TAG} -f Dockerfile .
                            docker push ${IMAGE_REPO}:${IMAGE_TAG}
                        """
                    }
                }
            }
        }
        stage('Deploy TO DEV'){
            when {
                expression { ref ==~ 'refs/heads/dev' }
                }
            environment{
                NAMESPACE = 'dev'
                INGRESS_HOST = "${INGRESS_HOST_PRE}.dev.devops.com"
                HELM_COMMON_ARGS = "${HELM_COMMON_ARGS} --set ingress.hosts[0].host=$INGRESS_HOST --set image.repository=$IMAGE_REPO --set image.tag=$ IMAGE_TAG"
            }
            steps{
                container('helm'){
                    script{
                        setupHelm()
                    }
                }
            }
        }
        stage('Deploy TO TEST'){
            when {
                expression { ref ==~ 'refs/heads/test' }
                }
            environment{
                NAMESPACE = 'test'
                INGRESS_HOST = "${INGRESS_HOST_PRE}.test.devops.com"
                HELM_COMMON_ARGS = "${HELM_COMMON_ARGS} --set ingress.hosts[0].host=$INGRESS_HOST --set image.repository=$IMAGE_REPO --set image.tag=$ IMAGE_TAG"
            }
            steps{
                container('helm'){
                    script{
                        setupHelm()
                    }
                }
            }
        }
        stage('Deploy TO UAT'){
            when {
                expression { ref ==~ 'refs/heads/uat' }
                }
            environment{
                NAMESPACE = 'uat'
                INGRESS_HOST = "${INGRESS_HOST_PRE}.uat.devops.com"
                HELM_COMMON_ARGS = "${HELM_COMMON_ARGS} --set ingress.hosts[0].host=$INGRESS_HOST --set image.repository=$IMAGE_REPO --set image.tag=$ IMAGE_TAG"
            }
            steps{
                container('helm'){
                    script{
                        setupHelm()
                    }
                }
            }
        }
        stage('Deploy TO PRE'){
            when {
                expression { ref ==~ 'refs/heads/pre' }
                }
            environment{
                NAMESPACE = 'pre'
                INGRESS_HOST = "${INGRESS_HOST_PRE}.pre.devops.com"
                HELM_COMMON_ARGS = "${HELM_COMMON_ARGS} --set ingress.hosts[0].host=$INGRESS_HOST --set image.repository=$IMAGE_REPO --set image.tag=$ IMAGE_TAG"
            }
            steps{
                container('helm'){
                    script{
                        setupHelm()
                    }
                }
            }
        }
        stage('Deploy TO PROD'){
            when {
                expression { ref ==~ 'refs/heads/prod' }
                }
            environment{
                NAMESPACE = 'prod'
                INGRESS_HOST = "${INGRESS_HOST_PRE}.devops.com"
                HELM_COMMON_ARGS = "${HELM_COMMON_ARGS} --set ingress.hosts[0].host=$INGRESS_HOST --set image.repository=$IMAGE_REPO --set image.tag=$ IMAGE_TAG"
            }
            steps{
                container('helm'){
                    script{
                        setupHelm()
                    }
                }
            }
        }
    }
}
}
```

The whole pipeline is: pull code -> compile -> build -> deploy. If we want to use Argocd, the only thing we have to change is the last step `deploy`. Instead of deploying it directly to Kubernetes, we modify the configuration in the `argocd-charts` project in Gitlab, and then Argocd synchronizes the configuration of that repository for deployment.

Then our entire process becomes the following:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/969ae6c742ea3c17b6f1ecc6cf40d0e2-0/wm)7

- Pull the code
- Compile the build, build the image and push it
- Change mirror information in helm chart's value.yaml, push to repository
- argocd monitors the chart repository for changes and updates the application

Our values.yaml file is in YAML format, and we can modify it directly with the `yq` command. So our deployed stage can look like this:

```groovy
        stage('Deploy TO DEV'){
            when {
                expression { ref ==~ 'refs/heads/dev' }
                }
            steps {
                container('yq'){
                    script{
                        sh """
                        git remote-set-url origin http://${GIT_USERNAME}:${GIT_PASSWORD}@${ARGOCD_CHARTS_URL}
                        git config --global user.name "${GIT_NAME}"
                        git config --global user.email "${GIT_EMAIL}"
                        git clone http://${GIT_USERNAME}:${GIT_PASSWORD}@${ARGOCD_CHARTS_URL} /opt/devops-cd
                        cd /opt/devops-cd/${APP_NAME}/charts
                        git pull
                        yq w --inplace dev.values.yaml 'image.repository' "${IMAGE_REPO}"
                        yq w --inplace dev.values.yaml 'image.tag' "${IMAGE_TAG}"
                        git commit -am '${APP_NAME} image update'
                        git push
                        """
                    }
                }
            }
        }
        stage('Deploy TO TEST'){
            when {
                expression { ref ==~ 'refs/heads/test' }
                }
            steps{
                container('yq'){
                    script{
                        sh """
                        git remote-set-url origin http://${GIT_USERNAME}:${GIT_PASSWORD}@${ARGOCD_CHARTS_URL}
                        git config --global user.name "${GIT_NAME}"
                        git config --global user.email "${GIT_EMAIL}"
                        git clone http://${GIT_USERNAME}:${GIT_PASSWORD}@${ARGOCD_CHARTS_URL} /opt/devops-cd
                        cd /opt/devops-cd/${APP_NAME}/charts
                        git pull
                        yq w --inplace test.values.yaml 'image.repository' "${IMAGE_REPO}"
                        yq w --inplace test.values.yaml 'image.tag' "${IMAGE_TAG}"
                        git commit -am '${APP_NAME} image update'
                        git push
                        """
                    }
                }
            }
        }
        stage('Deploy TO UAT'){
            when {
                expression { ref ==~ 'refs/heads/uat' }
                }
            steps{
                container('yq'){
                    script{
                        sh """
                        git remote-set-url origin http://${GIT_USERNAME}:${GIT_PASSWORD}@${ARGOCD_CHARTS_URL}
                        git config --global user.name "${GIT_NAME}"
                        git config --global user.email "${GIT_EMAIL}"
                        git clone http://${GIT_USERNAME}:${GIT_PASSWORD}@${ARGOCD_CHARTS_URL} /opt/devops-cd
                        cd /opt/devops-cd/${APP_NAME}/charts
                        git pull
                        yq w --inplace uat.values.yaml 'image.repository' "${IMAGE_REPO}"
                        yq w --inplace uat.values.yaml 'image.tag' "${IMAGE_TAG}"
                        git commit -am '${APP_NAME} image update'
                        git push
                        """
                    }
                }
            }
        }
        stage('Deploy TO PRE'){
            when {
                expression { ref ==~ 'refs/heads/pre' }
                }
            steps{
                container('yq'){
                    script{
                        sh """
                        git remote-set-url origin http://${GIT_USERNAME}:${GIT_PASSWORD}@${ARGOCD_CHARTS_URL}
                        git config --global user.name "${GIT_NAME}"
                        git config --global user.email "${GIT_EMAIL}"
                        git clone http://${GIT_USERNAME}:${GIT_PASSWORD}@${ARGOCD_CHARTS_URL} /opt/devops-cd
                        cd /opt/devops-cd/${APP_NAME}/charts
                        git pull
                        yq w --inplace pre.values.yaml 'image.repository' "${IMAGE_REPO}"
                        yq w --inplace pre.values.yaml 'image.tag' "${IMAGE_TAG}"
                        git commit -am '${APP_NAME} image update'
                        git push
                        """
                    }
                }
            }
        }
        stage('Deploy TO PROD'){
            when {
                expression { ref ==~ 'refs/heads/prod' }
                }
            steps{
                container('yq'){
                    script{
                        sh """
                        git remote-set-url origin http://${GIT_USERNAME}:${GIT_PASSWORD}@${ARGOCD_CHARTS_URL}
                        git config --global user.name "${GIT_NAME}"
                        git config --global user.email "${GIT_EMAIL}"
                        git clone http://${GIT_USERNAME}:${GIT_PASSWORD}@${ARGOCD_CHARTS_URL} /opt/devops-cd
                        cd /opt/devops-cd/${APP_NAME}/charts
                        git pull
                        yq w --inplace prod.values.yaml 'image.repository' "${IMAGE_REPO}"
                        yq w --inplace prod.values.yaml 'image.tag' "${IMAGE_TAG}"
                        git commit -am '${APP_NAME} image update'
                        git push
                        """
                    }
                }
            }
        }
```

But isn't this code awful, there is a lot of repetitive code in each stage, which can lead to a long and bloated pipeline.

To do this, we need to consolidate the duplicate code into a shared repository. Create a `vars/setupArgocd.groovy` file in Gitlab's `jenkins-sharelibrary` shared repository that looks like this:

```groovy
def call(){
    sh """
        git remote-set-url origin http://${GIT_USERNAME}:${GIT_PASSWORD}@${ARGOCD_CHARTS_URL}
        git config --global user.name "${GIT_NAME}"
        git config --global user.email "${GIT_EMAIL}"
        git clone http://${GIT_USERNAME}:${GIT_PASSWORD}@${ARGOCD_CHARTS_URL} /opt/devops-cd
        cd /opt/devops-cd/${APP_NAME}/charts
        git pull
        yq w --inplace ${HELM_VALUES_NAME} 'image.repository' "${IMAGE_REPO}"
        yq w --inplace ${HELM_VALUES_NAME} 'image.tag' "${IMAGE_TAG}"
        git commit -am "${APP_NAME} image update"
        git push
    """
}
```

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/dc1d70cbd522ed726a9670c561d56043-0/wm)

Then our deployment stage becomes the following:

```groovy
        stage('Deploy TO DEV'){
            when {
                expression { ref ==~ 'refs/heads/dev' }
                }
            environment {
                HELM_VALUES_NAME = "dev.values.yaml"
            }
            steps{
                container('yq'){
                    script{
                        setupArgocd()
                    }
                }
            }
        }
        stage('Deploy TO TEST'){
            when {
                expression { ref ==~ 'refs/heads/test' }
                }
            environment {
                HELM_VALUES_NAME = "test.values.yaml"
            }
            steps{
                container('yq'){
                    script{
                        setupArgocd()
                    }
                }
            }
        }
        stage('Deploy TO UAT'){
            when {
                expression { ref ==~ 'refs/heads/uat' }
                }
            environment {
                HELM_VALUES_NAME = "uat.values.yaml"
            }
            steps{
                container('yq'){
                    script{
                        setupArgocd()
                    }
                }
            }
        }
        stage('Deploy TO PRE'){
            when {
                expression { ref ==~ 'refs/heads/pre' }
                }
            environment {
                HELM_VALUES_NAME = "pre.values.yaml"
            }
            steps{
                container('yq'){
                    script{
                        setupArgocd()
                    }
                }
            }
        }
        stage('Deploy TO PROD'){
            when {
                expression { ref ==~ 'refs/heads/prod' }
                }
            environment {
                HELM_VALUES_NAME = "prod.values.yaml"
            }
            steps{
                container('yq'){
                    script{
                        setupArgocd()
                    }
                }
            }
        }

```

Finally, our entire pipeline is as follows:

```groovy
def call(params){

def tools = new org.devops.tools()

pipeline {
  agent {
        kubernetes {
            label "jenkins-slave-${UUUID.randomUUUID().toString()}"
            yaml """
apiVersion: v1
kind: Pod
spec.
  containers.
  - name: golang
    image: registry.cn-hangzhou.aliyuncs.com/coolops/golang:1.18.5
    command: ['cat']
    tty: true
  - name: docker
    image: registry.cn-hangzhou.aliyuncs.com/coolops/docker:19.03.11
    command: ['cat']
    tty: true
    volumeMounts.
      - name: indocker
        mountPath: /var/run/docker.sock
  - name: yq
    image: registry.cn-hangzhou.aliyuncs.com/coolops/helm-kubectl-curl-git-jq-yq:latest
    command: ['cat']
    tty: true
  volumes.
    - name: indocker
      hostPath.
        path: "/var/run/docker.sock"
"""
        }
    }

    environment{
        APP_NAME = "${params.APP_NAME}"
        INGRESS_HOST_PRE = "${params.INGRESS_HOST_PRE}"
        INGRESS_ENABLE = "${params.INGRESS_ENABLE? params.INGRESS_ENABLE :false}"
        IMAGE_REPO = ""
        IMAGE_TAG = ""
        GIT_USERNAME = "root"
        GIT_PASSWORD = "admin321"
        GIT_NAME = "joker"
        GIT_EMAIL = "joker@devops.com"
        ARGOCD_CHARTS_URL = "10.111.127.141:30180/devops/argocd-charts.git"

        // Mirror repository configuration
        REGISTRY_URL = "10.111.127.141:30002"
        REGISTRY_USERNAME = "admin"
        REGISTRY_PASSWORD = "Harbor12345"

        HELM_COMMON_ARGS= "--set ingress.enabled=$INGRESS_ENABLE \
                           --set containers.port=8080 \
                           ---set containers.healthCheak.path=/health \
                           --set ingress.hosts[0].paths[0].path=/ \
                           --set ingress.hosts[0].paths[0].pathType=ImplementationSpecific deploy/charts/ "
    }

    triggers {
        GenericTrigger(
        genericVariables: [
        [key: 'ref', value: '$.ref']
        ].
        causeString: 'Triggered on $ref'.
        token: 'go-hello-world'.
        printContributedVariables: true.
        printPostContent: true.
        silentResponse: false.
        regexpFilterText: '$ref'.
        regexpFilterExpression: 'refs/heads/(dev|test|uat|pre|prod)'
        )
    }

    stages {
        stage('Get Code') {
            steps {
                checkout(scm)
            }
        }

        stage('Get Image Repo') {
            steps {
                script{
                    BRANCH = ref - "refs/heads/"
                    IMAGE_REPO = "${REGISTRY_URL}/${BRANCH}/${APP_NAME}"
                }
            }
        }

        stage('Build Code') {
            steps {
                container('golang'){
                    script{
                        sh '''
                            export GOPROXY=https://goproxy.cn
                            export GOOS=linux
                            export GOARCH=386
                            go mod tidy
                            go build -v -o . /${APP_NAME}
                        '''
                    }
                }
            }
        }
        stage('Build And Push Image') {
            steps {
                container('docker'){
                    script{

                        IMAGE_TAG = tools.createImageTag()
                        sh """
                            docker login ${REGISTRY_URL} -u ${REGISTRY_USERNAME} -p ${REGISTRY_PASSWORD}
                            docker build -t ${IMAGE_REPO}:${IMAGE_TAG} -f Dockerfile .
                            docker push ${IMAGE_REPO}:${IMAGE_TAG}
                        """
                    }
                }
            }
        }
        stage('Deploy TO DEV'){
            when {
                expression { ref ==~ 'refs/heads/dev' }
                }
            environment {
                HELM_VALUES_NAME = "dev.values.yaml"
                IMAGE_REPO = "${IMAGE_REPO}"
                IMAGE_TAG = "${IMAGE_TAG}"
            }
            steps{
                container('yq'){
                    script{
                        setupArgocd()
                    }
                }
            }
        }
        stage('Deploy TO TEST'){
            when {
                expression { ref ==~ 'refs/heads/test' }
                }
            environment {
                HELM_VALUES_NAME = "test.values.yaml"
                IMAGE_REPO = "${IMAGE_REPO}"
                IMAGE_TAG = "${IMAGE_TAG}"
            }
            steps{
                container('yq'){
                    script{
                        setupArgocd()
                    }
                }
            }
        }
        stage('Deploy TO UAT'){
            when {
                expression { ref ==~ 'refs/heads/uat' }
                }
            environment {
                HELM_VALUES_NAME = "uat.values.yaml"
                IMAGE_REPO = "${IMAGE_REPO}"
                IMAGE_TAG = "${IMAGE_TAG}"
            }
            steps{
                container('yq'){
                    script{
                        setupArgocd()
                    }
                }
            }
        }
        stage('Deploy TO PRE'){
            when {
                expression { ref ==~ 'refs/heads/pre' }
                }
            environment {
                HELM_VALUES_NAME = "pre.values.yaml"
                IMAGE_REPO = "${IMAGE_REPO}"
                IMAGE_TAG = "${IMAGE_TAG}"
            }
            steps{
                container('yq'){
                    script{
                        setupArgocd()
                    }
                }
            }
        }
        stage('Deploy TO PROD'){
            when {
                expression { ref ==~ 'refs/heads/prod' }
                }
            environment {
                HELM_VALUES_NAME = "prod.values.yaml"
                IMAGE_REPO = "${IMAGE_REPO}"
                IMAGE_TAG = "${IMAGE_TAG}"
            }
            steps{
                container('yq'){
                    script{
                        setupArgocd()
                    }
                }
            }
        }
    }
}
}
```

Then save the above to the `vars/goDeployByArgocd.groovy` file in Gitlab's `jenkins-sharelibrary` shared repository, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/4d9bdc6cfa4fc12cde23105a22758628-0/wm)

Then change the Jenkinsfile in the `go-hello-world` project to the following:

```groovy
@Library('sharelibrary') _
def BuildEnv = [APP_NAME: "go-hello-world",INGRESS_HOST_PRE: "hello",INGRESS_ENABLE:true]
goDeployByArgocd(BuildEnv)
```

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/2d62d3f1bd552595d06bfa9d67c763a3-0/wm)
