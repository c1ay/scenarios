### Jenkins testing

Now, let's create a simple `free style` project to test that Jenkins is working properly.

First click **New item** to create a task.

![图片描述](assets/lab-deploying-and-using-jenkins-in-kubernetes-7-0.png)

Enter the task name and select the free style

![图片描述](assets/lab-deploying-and-using-jenkins-in-kubernetes-7-1.png)

Pull down to the bottom **Build**, select **Execute Shell** and type `echo 'Hello world'`, as follows:

![图片描述](assets/lab-deploying-and-using-jenkins-in-kubernetes-7-2.png)

Click Save and the first pipeline is created.

Click **Build Now** to execute the pipeline.

![图片描述](assets/lab-deploying-and-using-jenkins-in-kubernetes-7-3.png)

After clicking on the build, the build history is displayed as follows:

![图片描述](assets/lab-deploying-and-using-jenkins-in-kubernetes-7-4.png)

Select the build sequence and select **console output** to see the output log, as follows:

![图片描述](assets/lab-deploying-and-using-jenkins-in-kubernetes-7-5.png)

You can tell from the output that the pipeline build was successful, indicating that Jenkins is working properly.
