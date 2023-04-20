### Jenkins testing

Now, let's create a simple `free style` project to test that Jenkins is working properly.

First click **New item** to create a task.

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/85c1d29638b1ba870698e7b8db523b87-0/wm)

Enter the task name and select the free style

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/de9c988b94557f117a42848d3dc5d0f0-0/wm)

Pull down to the bottom **Build**, select **Execute Shell** and type `echo 'Hello world'`, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/4d990c40dddda021dabf550655b7c78a-0/wm)

Click Save and the first pipeline is created.

Click **Build Now** to execute the pipeline.

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/1acedddaa9ea78ebabf4b249be961e44-0/wm)

After clicking on the build, the build history is displayed as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/b154bbbfb82bfb010f53373f4b150eec-0/wm)

Select the build sequence and select **console output** to see the output log, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/10c18106574521fd2860430fd5a38117-0/wm)

You can tell from the output that the pipeline build was successful, indicating that Jenkins is working properly.
