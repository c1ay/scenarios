### Configuring Webhook on Gitlab

Find the `test-gitlab-hook` project, select `settings` -> `integrations`, and go to the following screen:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/019e70e3882f3f99b4f4174b264d4ae6-0/wm)

> PS: In the newer versions of Gitlab, it's called `webhooks`.

Then fill in the `webhook url` and `token` as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/5e71924a7eedb393d2c0d766df86878d-0/wm)

where `Webhook url` and `token` are both found in the Jenkins project.

Pull them down, uncheck SSL and add them.

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/964454754bfbc763e23e128f40435770-0/wm)

However, since Gitlab and Jenkins are on the same network, the default is to report an error with the following message:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/4bfa1cc2ee97cb1573731b4c0e21a061-0/wm)

Select **System Settings** -> **Network** -> **outbound requests** and choose to expand it as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/8fbb39b261d528e708437f190e06e600-0/wm)

Then select **allow local network requests** and click save, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/2e637ed1a06182d55a4d829edd9ebe3e-0/wm)

Now come back and add the Webhook without any problem, as follows to indicate successful addition.

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/14bf93b4cce3afd22decc4bc5c379be7-0/wm)

We select `Test` -> `Push Events` to test that the Webhook is working properly, and see on Jenkins that the pipeline is being triggered automatically, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/2226a1c5b01e4e5bf89daec7bdc90b30-0/wm)

Now the integration between Gitlab and Jenkins is complete.
