### Create a simple Pipeline

Select **New Task**, enter the task name, and select **Pipeline** as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/fab12dc90be2edf3e055be9657cdc8b8-0/wm)

Then pull up to the **Pipeline** configuration and enter the following:

```groovy
pipeline{
    agent any
    stages{
        stage("GetCode"){
            steps{
                sh "echo 'Get Code' " //step
            }
        }

        stage("build"){
            steps{
                sh "echo 'Build Code' " //step
            }
        }

        stage("push"){
            steps{
                sh "echo 'Build Image' " //step
            }
        }

        stage("deploy"){
            steps{
                sh "echo 'Deploy app' " //step
            }
        }
    }
}
```

The results are as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/f576e4e7d555138f076529eed113eec9-0/wm)

Then click **Save** and select **Build Now** in the project to see the build results, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/f4a9ad7eb662f82cd610def010761529-0/wm)

In the **red box** you can see the exact steps and how long each step took.

At **build history** you can select the history ID to view the build log, the output is as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/7de092d8be7dace3b3377d4ac898040e-0/wm)

To run it in the Jenkins Slave we configured earlier, i.e. using the dynamic Slave, simply change the script to the following:

```groovy
pipeline{
    agent {
        label 'jenkins-jnlp'
    }
    stages{
        stage("GetCode"){
            steps{
                sh "echo 'Get Code' " //step
            }
        }

        stage("build"){
            steps{
                sh "echo 'Build Code' " //step
            }
        }

        stage("push"){
            steps{
                sh "echo 'Build Image' " //step
            }
        }

        stage("deploy"){
            steps{
                sh "echo 'Deploy app' " //step
            }
        }
    }
}
```
