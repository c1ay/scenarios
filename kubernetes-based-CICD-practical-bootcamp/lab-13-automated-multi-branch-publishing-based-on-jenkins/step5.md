### Splice mirror repositories

Since we want to implement pushing mirrors from different branches to different repositories, we need to determine the mirror repository before the mirror build, and for that we need to add a stage as follows:

```groovy
    stage('Get Image Repo') {
        steps {
            script{
                BRANCH = ref - "refs/heads/"
                IMAGE_REPO = "10.111.127.141:30002/${BRANCH}/go-hello-world"
            }
        }
    }
```
