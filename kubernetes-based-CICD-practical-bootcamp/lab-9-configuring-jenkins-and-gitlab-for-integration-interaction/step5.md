### Configuring Webhook on Gitlab

Find the `test-gitlab-hook` project, select `settings` -> `integrations`, and go to the following screen:

![图片描述](assets/lab-configuring-jenkins-and-gitlab-for-integration-interaction-4-0.png)

> PS: In the newer versions of Gitlab, it's called `webhooks`.

Then fill in the `webhook url` and `token` as follows:

![图片描述](assets/lab-configuring-jenkins-and-gitlab-for-integration-interaction-4-1.png)

where `Webhook url` and `token` are both found in the Jenkins project.

Pull them down, uncheck SSL and add them.

![图片描述](assets/lab-configuring-jenkins-and-gitlab-for-integration-interaction-4-2.png)

However, since Gitlab and Jenkins are on the same network, the default is to report an error with the following message:

![图片描述](assets/lab-configuring-jenkins-and-gitlab-for-integration-interaction-4-3.png)

Select **System Settings** -> **Network** -> **outbound requests** and choose to expand it as follows:

![图片描述](assets/lab-configuring-jenkins-and-gitlab-for-integration-interaction-4-4.png)

Then select **allow local network requests** and click save, as follows:

![图片描述](assets/lab-configuring-jenkins-and-gitlab-for-integration-interaction-4-5.png)

Now come back and add the Webhook without any problem, as follows to indicate successful addition.

![图片描述](assets/lab-configuring-jenkins-and-gitlab-for-integration-interaction-4-6.png)

We select `Test` -> `Push Events` to test if the Webhook is working properly, and see on Jenkins that the pipeline is triggered automatically, as follows:

![图片描述](assets/lab-configuring-jenkins-and-gitlab-for-integration-interaction-4-7.png)

Now the integration between Gitlab and Jenkins is complete.
