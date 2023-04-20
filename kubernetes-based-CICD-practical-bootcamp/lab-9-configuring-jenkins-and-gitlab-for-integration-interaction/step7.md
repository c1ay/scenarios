### Installing the Generic Webhook plugin

Select **System Configuration** -> **Plugin Management** on Jenkins, search for `Generic Webhook Trigger` at **Optional Plugins** and install it, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/e7cc1b2c5cdbbaa2428832214ea2cc62-0/wm)

After the installation is complete, restart Jenkins.

After the plugin is installed, there will be an additional `Generic Webhook Trigger` on the task configuration page, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/7db75a0a0d3b659a21893a8709f50f52-0/wm)

where `http://JENKINS_URL/generic-webhook-trigger/invoke` is a fixed format for triggering a Webhook, followed by a Token, e.g. `http://localhost:8080/generic-webhook-trigger /invoke?token=abc123`.
