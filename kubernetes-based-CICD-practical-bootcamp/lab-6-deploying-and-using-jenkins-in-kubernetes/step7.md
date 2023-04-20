## Jenkins initialization

Since our Jenkins is exposed directly using Service NodePort, we can access it directly using `http://10.111.127.141:30880`, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/5fb80668446fc8cb8dc9ecac122a88d2-0/wm)

To log in and get the admin key, you can directly use `kubectl logs -n devops [POD_NAME]` to see the key, as follows

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/94a7e8c5650c699d412b012856e5575b-0/wm)

Copy the key to your browser, fill it in and continue to the plugin installation screen, then select `Install recommended plugins`, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/d302f19796183a599c4ca81a51f7fc29-0/wm)

Then it will follow the default plugin and wait for the installation to complete, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/156abc9d7667a71ddcc47888453de308-0/wm)

Then create an administrator account, fill in the specific information, and click Save, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/b6260fd3ca56935fc4a7282ffd129d7f-0/wm)

Configure the Jenkins address, the default is fine, as follows

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/dff0ba33c670e44878f11feaf1b97cf8-0/wm)

Then click **Start Using Jenkins** to complete the initialization of Jenkins and enter the Jenkins interface, as follows

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/74e31057ae1de4080121226788d217f7-0/wm)
