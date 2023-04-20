### Create and configure the project on Jenkins

Select **New Task**, enter a task name, and select **Free Style Project** as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/378308998ccaa92b6f3b1ecce6252c5a-0/wm)

Then select `Build when a change is pushed to Gitlab` at the **Build Trigger** as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/1f986b5c065825f1d0c3a7723f873411-0/wm)

where `Gitlab webhook URL` is the webhook address for the project.

For the rest of the configuration select the default, then select **Advanced** as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/630d7090efdc2360be0c93a9d557351c-0/wm)

Selecting `Generate` at `Secret token` will generate a Token, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/dfa7de5875c1b920daad90392472a4d0-0/wm)

Select `Build` -> `Execute shell` and enter the following:

```shell
echo "auto build"
```

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/31a08a1b2b259893f552dbb98aa1c981-0/wm)

Fill in the source code in **Source Code Manager** and configure it as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/0ca969cc2cf928870ff870102684cfe7-0/wm)

After the configuration, save and exit.
