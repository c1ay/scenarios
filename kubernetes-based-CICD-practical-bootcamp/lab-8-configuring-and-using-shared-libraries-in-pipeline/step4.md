### Stage

stage defines the conceptual different stages of the execution of tasks throughout the pipeline. For example: GetCode, Build, Test, Deploy, CodeScan Each stage, as follows:

```groovy
pipeline{
    agent any
    stages{
        stage("GetCode"){
        //code area
        }
        stage("Build"){
        // code area
        }
    }
}
```
