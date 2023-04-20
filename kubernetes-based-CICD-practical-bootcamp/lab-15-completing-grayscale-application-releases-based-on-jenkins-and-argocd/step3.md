## Create a pipeline on Jenkins

In the previous section, we used an auto-triggered pipeline to build, but for this experiment we'll change it to a manual branch selection build, for which we need to modify the pipeline to

- Branch parameters need to be passed in
- The code to be pulled should be pulled by branch

The branch is passed in through the parameters, and the code is as follows:

```groovy
    parameters {
        choice(description: 'Please choose a branch', name: 'branch', choices: ['dev', 'test', 'uat', 'pre', 'prod'])
    }
```

The pull code is pulled by branch, with the following code:

```groovy
 checkout([$class: 'GitSCM', branches: [[name: "${branch}"]], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: []. userRemoteConfigs: [[credentialsId: 'gitlab', url: "${GITLAB_URL}"]]])
```

So our entire pipeline changes to the following:

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
        GITLAB_URL = "${params.GITLAB_URL}"
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

    parameters {
        choice(description: 'Please select branch', name: 'branch', choices: ['dev', 'test', 'uat', 'pre', 'prod'])
    }

    stages {
        stage('Get Code') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: "${branch}"]], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: []. userRemoteConfigs: [[credentialsId: 'gitlab', url: "${GITLAB_URL}"]]])
            }
        }

        stage('Get Image Repo') {
            steps {
                script{
                    BRANCH = "${branch}"
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
                expression { branch ==~ 'dev' }
                }
            environment {
                HELM_VALUES_NAME = "dev.values.yaml"
                IMAGE_REPO = "${IMAGE_REPO}"
                IMAGE_TAG = "${IMAGE_TAG}"
            }
            steps{
                container('yq'){
                    script{
                        setupRolloutArgocd()
                    }
                }
            }
        }
        stage('Deploy TO TEST'){
            when {
                expression { branch ==~ 'test' }
                }
            environment {
                HELM_VALUES_NAME = "test.values.yaml"
                IMAGE_REPO = "${IMAGE_REPO}"
                IMAGE_TAG = "${IMAGE_TAG}"
            }
            steps{
                container('yq'){
                    script{
                        setupRolloutArgocd()
                    }
                }
            }
        }
        stage('Deploy TO UAT'){
            when {
                expression { branch ==~ 'uat' }
                }
            environment {
                HELM_VALUES_NAME = "uat.values.yaml"
                IMAGE_REPO = "${IMAGE_REPO}"
                IMAGE_TAG = "${IMAGE_TAG}"
            }
            steps{
                container('yq'){
                    script{
                        setupRolloutArgocd()
                    }
                }
            }
        }
        stage('Deploy TO PRE'){
            when {
                expression { branch ==~ 'pre' }
                }
            environment {
                HELM_VALUES_NAME = "pre.values.yaml"
                IMAGE_REPO = "${IMAGE_REPO}"
                IMAGE_TAG = "${IMAGE_TAG}"
            }
            steps{
                container('yq'){
                    script{
                        setupRolloutArgocd()
                    }
                }
            }
        }
        stage('Deploy TO PROD'){
            when {
                expression { branch ==~ 'prod' }
                }
            environment {
                HELM_VALUES_NAME = "prod.values.yaml"
                IMAGE_REPO = "${IMAGE_REPO}"
                IMAGE_TAG = "${IMAGE_TAG}"
            }
            steps{
                container('yq'){
                    script{
                        setupRolloutArgocd()
                    }
                }
            }
        }
    }
}
}
```

Then save it to the `vars/goDeployByArgoRollout.groovy` file in the Jenkins shared library `jenkins-sharelibrary`, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/0bab3967abacef69feeb158312ba2be2-0/wm)

Then create `vars/setupRolloutArgocd.groovy` in the shared library and save the following:

```groovy
def call(){
    sh """
        git remote-set-url origin http://${GIT_USERNAME}:${GIT_PASSWORD}@${ARGOCD_CHARTS_URL}
        git config --global user.name "${GIT_NAME}"
        git config --global user.email "${GIT_EMAIL}"
        git clone http://${GIT_USERNAME}:${GIT_PASSWORD}@${ARGOCD_CHARTS_URL} /opt/devops-cd
        cd /opt/devops-cd/argocd-rollout-charts/${APP_NAME}/charts
        git pull
        yq w --inplace ${HELM_VALUES_NAME} 'image.repository' "${IMAGE_REPO}"
        yq w --inplace ${HELM_VALUES_NAME} 'image.tag' "${IMAGE_TAG}"
        git commit -am "${APP_NAME} image update"
        git push
    """
}
```

> PS: setupRolloutArgocd and setupArgocd two methods in the content is almost identical, only a small path difference, in fact, can be completely synthesized into one, I recreated a for convenience, you can consider how to integrate into a method.

Create a `rollout.Jenkinsfile` in the master branch of the `go-hello-world` project in Gitlab, and write the following:

```groovy
@Library('sharelibrary') _
def BuildEnv = [APP_NAME: "go-hello-world",INGRESS_HOST_PRE: "hello",INGRESS_ENABLE:true,GITLAB_URL: "http://10.111.127.141:30180/devops /go-hello-world.git"]
goDeployByArgoRollout(BuildEnv)
```

Create the `go-hello-world-rollout` project on Jenkins with the following configuration:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/bc98c9717e900dbb5dfa22fc36be30c9-0/wm)

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/0b037fd57615e8058d8e90f2ad2a0488-0/wm)

> PS: Note that the script path is no longer Jenkinsfile, but rollout.Jenkinsfile.

Then save and exit, executing it once to let Jenkins finish loading the configuration parameters, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/66a477507c810e5f233402ab83a24d7b-0/wm)

Then run the pipeline again, select the `dev` branch, and see if the Jenkins logs are correct.

- First check to see if you are pulling code from the `dev` branch

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/4e2c397cfeeb474b1fcaad0901eeb49d-0/wm)

- To see if it is deployed to a `dev` environment

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/9aaa5c46a2be0757f4ccc68a504e53af-0/wm)

As above, the pipeline is fine.

Then go to Argocd to check if the application can be updated properly, click on the project to enter the details screen, we can see that the rollout is in the pause stage, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/0646c2555e93232c0109cdc94d43dc26-0/wm)

Normally, if the version is OK, we need to execute `kubectl argo rollouts promote go-hello-world-rollout` on the command line to continue the update, but there is a button provided on Argocd, as follows

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/a88e5a6c6db52b9c7a1d77e3a45d2869-0/wm)

We just need to click this button to continue the update, and then the whole application becomes up-to-date as follows

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/d4561f3b96d9087f02e4856feef6e3e4-0/wm)
