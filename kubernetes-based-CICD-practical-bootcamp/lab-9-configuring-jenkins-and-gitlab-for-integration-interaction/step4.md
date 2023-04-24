### Create and configure the project on Jenkins

Select **New Task**, enter a task name, and select **Free Style Project** as follows:

![图片描述](assets/lab-configuring-jenkins-and-gitlab-for-integration-interaction-3-0.png)

Then select `Build when a change is pushed to Gitlab` at the **Build Trigger** as follows:

![图片描述](assets/lab-configuring-jenkins-and-gitlab-for-integration-interaction-3-1.png)

where `Gitlab webhook URL` is the webhook address for the project.

For the rest of the configuration select the default, then select **Advanced** as follows:

![图片描述](assets/lab-configuring-jenkins-and-gitlab-for-integration-interaction-3-2.png)

Selecting `Generate` at `Secret token` will generate a Token, as follows:

![图片描述](assets/lab-configuring-jenkins-and-gitlab-for-integration-interaction-3-3.png)

Select `Build` -> `Execute shell` and enter the following:

```shell
echo "auto build"
```

![图片描述](assets/lab-configuring-jenkins-and-gitlab-for-integration-interaction-3-4.png)

Fill in the source code in **Source Code Manager** and configure it as follows:

![图片描述](assets/lab-configuring-jenkins-and-gitlab-for-integration-interaction-3-5.png)

After the configuration, save and exit.
