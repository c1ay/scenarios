### Step

step is each step to be executed in each phase, e.g:

```groovy
pipeline{
    agent any
    stages{
        stage("GetCode"){
            steps{
                sh "ls " //step
            }
        }
    }
}
```
