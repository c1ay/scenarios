### Add multi-branch deployment

For multi-branch deployment, we implement it by means of conditional judgments, i.e. adding several stages, and using when for each stage, as follows

```groovy
    stage('Deploy TO DEV'){
        when {
            expression { ref ==~ 'refs/heads/dev' }
            }
        steps {
            container('helm'){
                script{
                    sh """
                        helm upgrade --install go-hello-world -n dev \
                        --set image.repository=${IMAGE_REPO} \
                        --set image.tag=${IMAGE_TAG} \
                        --set containers.port=8080 \
                        --set containers.healthCheak.path=/health \
                        --set ingress.enabled=true \
                        --set ingress.hosts[0].host=hello.dev.devops.com \
                        --set ingress.hosts[0].paths[0].path=/ \
                        --set ingress.hosts[0].paths[0].pathType=ImplementationSpecific deploy/charts/
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
            container('helm'){
                script{
                    sh """
                        helm upgrade --install go-hello-world -n test \
                        --set image.repository=${IMAGE_REPO} \
                        --set image.tag=${IMAGE_TAG} \
                        --set containers.port=8080 \
                        --set containers.healthCheak.path=/health \
                        --set ingress.enabled=true \
                        --set ingress.hosts[0].host=hello.test.devops.com \
                        --set ingress.hosts[0].paths[0].path=/ \
                        --set ingress.hosts[0].paths[0].pathType=ImplementationSpecific deploy/charts/
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
            container('helm'){
                script{
                    sh """
                        helm upgrade --install go-hello-world -n uat \
                        --set image.repository=${IMAGE_REPO} \
                        --set image.tag=${IMAGE_TAG} \
                        --set containers.port=8080 \
                        --set containers.healthCheak.path=/health \
                        --set ingress.enabled=true \
                        --set ingress.hosts[0].host=hello.uat.devops.com \
                        --set ingress.hosts[0].paths[0].path=/ \
                        --set ingress.hosts[0].paths[0].pathType=ImplementationSpecific deploy/charts/
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
            container('helm'){
                script{
                    sh """
                        helm upgrade --install go-hello-world -n pre \
                        --set image.repository=${IMAGE_REPO} \
                        --set image.tag=${IMAGE_TAG} \
                        --set containers.port=8080 \
                        --set containers.healthCheak.path=/health \
                        --set ingress.enabled=true \
                        --set ingress.hosts[0].host=hello.pre.devops.com \
                        --set ingress.hosts[0].paths[0].path=/ \
                        --set ingress.hosts[0].paths[0].pathType=ImplementationSpecific deploy/charts/
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
            container('helm'){
                script{
                    sh """
                        helm upgrade --install go-hello-world -n prod \
                        --set image.repository=${IMAGE_REPO} \
                        --set image.tag=${IMAGE_TAG} \
                        --set containers.port=8080 \
                        --set containers.healthCheak.path=/health \
                        --set ingress.enabled=true \
                        --set ingress.hosts[0].host=hello.prod.devops.com \
                        --set ingress.hosts[0].paths[0].path=/ \
                        --set ingress.hosts[0].paths[0].pathType=ImplementationSpecific deploy/charts/
                    """
                }
            }
        }
    }
```

Why do we need so many stages here, can't we use one?

One is definitely possible, but the configuration of different environment applications may be different, if you use a stage will need to do a high degree of abstraction, in order to facilitate the definition of different environments, so the definition of different stages for different environments.
