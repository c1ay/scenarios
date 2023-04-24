## Jenkins initialization

Since our Jenkins is exposed directly using Service NodePort, we can access it directly using `http://10.111.127.141:30880`, as follows:

![图片描述](assets/lab-deploying-and-using-jenkins-in-kubernetes-6-0.png)

To log in and get the admin key, you can directly use `kubectl logs -n devops [POD_NAME]` to see the key, as follows

![图片描述](assets/lab-deploying-and-using-jenkins-in-kubernetes-6-1.png)

Copy the key to your browser, fill it in and continue to the plugin installation screen, then select `Install recommended plugins`, as follows:

![图片描述](assets/lab-deploying-and-using-jenkins-in-kubernetes-6-2.png)

Then it will follow the default plugin and wait for the installation to complete, as follows:

![图片描述](assets/lab-deploying-and-using-jenkins-in-kubernetes-6-3.png)

Then create an administrator account, fill in the specific information, and click Save, as follows:

![图片描述](assets/lab-deploying-and-using-jenkins-in-kubernetes-6-4.png)

Configure the Jenkins address, the default is fine, as follows

![图片描述](assets/lab-deploying-and-using-jenkins-in-kubernetes-6-5.png)

Then click **Start Using Jenkins** to complete the initialization of Jenkins and enter the Jenkins interface, as follows

![图片描述](assets/lab-deploying-and-using-jenkins-in-kubernetes-6-6.png)
