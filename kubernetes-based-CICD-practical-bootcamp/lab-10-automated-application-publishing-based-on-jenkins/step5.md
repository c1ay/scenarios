### Build the image and push it

To build and push the image, you need to use the docker command, we use `Docker in Docker` here, so just use the command directly, the script code is as follows:

```groovy
@Library('sharelibrary')

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

  stages {
    stage('Get Code') {
        steps {
            checkout(scm)
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
                        go build -v -o . /go-hello-world
                    '''
                }
            }
        }
    }
    stage('Build And Push Image') {
        steps {
            container('docker'){
                script{
                    IMAGE_REPO="10.111.127.141:30002/dev/go-hello-world"
                    IMAGE_TAG=tools.createImageTag()
                    sh """
                        docker login 10.111.127.141:30002 -u admin -p Harbor12345
                        docker build -t ${IMAGE_REPO}:${IMAGE_TAG} -f Dockerfile .
                        docker push ${IMAGE_REPO}:${IMAGE_TAG}
                    """
                }
            }
        }
    }
    stage('Deploy'){
        steps{
            container('helm'){
                script{
                    print('Deploy Application')
                }
            }
        }
    }
  }
}
```

We used `tools.createImageTag` above to create the image's Tag, and this method is defined in the shared library, so you need to add the following code to `src/org/devops/tools.groovy` in the shared library `jenkins-sharelibrary`:

```groovy
// Get the image version
def createImageTag() {
    return new Date().format('yyyyMMddHHmmss') + "_${env.BUILD_ID}"
}
```

And it needs to reference the `shared library`, so the following code is added at the top of the Pipeline:

```groovy
@Library('sharedlibrary')

def tools = new org.devops.tools()
```

Then pushing the image requires a login, so here we use `docker login` directly for convenience.

Finally, use the Pipeline above to override the Jenkinsfile in the `go-hello-world` project, build the project and observe the logs:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/e8c7f1607d9f35656332fb8c8d39d12a-0/wm)
