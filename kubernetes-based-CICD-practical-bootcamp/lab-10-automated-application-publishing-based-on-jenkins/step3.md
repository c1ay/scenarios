### Pull the code

To pull code, we use `checkout`, which can be generated using **pipeline syntax** as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/089a94e74f5cbffadab74cf1f2bdd5da-0/wm)

Then click on **generate pipeline script** below to generate the code, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/c684b4841f076112bc5bec3f10380eb0-0/wm)

However, I'm going to put `Jenkinsfile` directly into the code repository here, so **pull code** just needs to be configured as follows:

```groovy
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
                    print('Build Code')
                }
            }
        }
    }
    stage('Build And Push Image') {
        steps {
            container('docker'){
                script{
                    print('Build And Push Image')
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

Then save the above to the `go-hello-world` project's `Jenkinsfile`, replace the previous content, and run the build on Jenkins. The build succeeds and the log output is as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/852aeee85c3ff4ed7a42f03a58b88390-0/wm)

This means that pulling the application code is fine.
