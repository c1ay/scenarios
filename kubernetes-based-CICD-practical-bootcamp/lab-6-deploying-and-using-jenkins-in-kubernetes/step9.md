## Configuring Slave

Previously, when deploying Jenkins on a physical machine, you would use a static Slave, i.e. configure jenkins-agent on a defined node, which had some problems, such as

- Each Slave has a different configuration environment to complete operations such as compilation and packaging in different languages, but these differing configurations make it very inconvenient to manage and laborious to maintain.
- Unbalanced resource allocation, some Slave to run the job appears to wait in line, while some Slave is idle.
- Resources are wasted, each Slave may be a physical machine or a virtual machine, and when the Slave is idle, the resources are not completely released.

For this reason, in Kubernetes, we use the dynamic Slave model, which creates Slave only when the pipeline is running, and dries up the Slave when the pipeline is finished, with the following logic diagram:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/afd88bc2eef96ab40ad925b315b0cbb8-0/wm)

This approach has the following advantages:

- When the Jenkins Master fails, Kubernetes automatically creates a new Jenkins Master container and assigns the Volume to the newly created container, ensuring that no data is lost, thus achieving high availability of the cluster services.
- Kubernetes dynamically assigns Slave to a free node based on the usage of each resource, reducing the risk of a node with high resource utilization. Kubernetes dynamically assigns Slave to a free node based on each resource usage, reducing the risk of waiting in line for a node with high resource utilization.
- Scalability: When a Kubernetes cluster is severely under-resourced and a Job is queued, it is easy to add a Kubernetes Node to the cluster, thus enabling scaling.

#### Installing the kubernetes plugin

Select **System Administration** -> **Plugin Management** -> **Optional Plugins**, search for `kubernetes`, select the plugin and click Install, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/1822f94f44592273c971eff1914fc605-0/wm)

Wait for its installation and reboot to complete.

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/b1dc625b59302f53e9e0a88dced93440-0/wm)

#### Configuring the Kubernetes Plugin

Select **System Administration** -> **Node Administration** -> **Configure Clouds** and select `kubernetes` in Configure Cluster as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/5664c936face3a109eeb69ce9c6fdbea-0/wm)

Then configure the Kubernetes address (internal address) and the namespace where the Slave will run, as follows

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/f80f1bbe5c4993f09c13f8b17ab59164-0/wm)

Click **Connect Test** to see the communication status of Jenkins and the Kubernetes cluster, when the result is `Connected to Kubernetes xxx` it means that the connectivity is normal, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/b7b5230bd191261e7e376bebcd582cc0-0/wm)

> PS: If the connection test fails, it's probably a permission issue, so we need to add the ServiceAccount credentials jenkins-sa to it.

To add the Jenkins address, just fill in the Service address, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/aeeabd00c6d1e22100e17f6653db46c0-0/wm)

Select `Pod Templates` and add the Slave Pod template, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/815e1cb0470831adb8c17a0278ad1293-0/wm)

Select **Add Template** and configure as required, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/42edc650f606d8af602322930a4164b5-0/wm)

Add the container template, the image `registry.cn-hangzhou.aliyuncs.com/coolops/jenkins:jnlp6` contains the Jenkins Slave client, and also the docker and kubectl commands, as follows

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/2b077907c03c01df7cb8b65bde737486-0/wm)

where:

- The run command is: `jenkins-slave`
- The command parameter is: `${computer.jnlpmac} ${computer.name}`

Two additional host directories need to be mounted:

1. `/var/run/docker.sock`: this file is used for the containers in the Pod to be able to share the Docker of the host;
1. `/home/shiyanlou/.kube`: this directory is mounted under the `/root/.kube` directory of the container This is so that we can use the kubectl tool to access our Kubernetes cluster in the container of the Pod, so that we can deploy Kubernetes in the Slave Pod later applications;

As follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/eb62cb64ef9a82a18f014680807bcf17-0/wm)

Finally, add `Service Account` to provide permissions to perform operations on Kubernetes, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/72296173e053d07a3195e1c2f307ed81-0/wm)

Click `Save` to complete the Kubernetes plug-in configuration.

#### Testing the Kubernetes plugin

Go back to Dashboard, select **New Task** and enter `test-kubernetes-slave`, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/0faac551da5cf1598e42f0e4c03053c0-0/wm)

Select the node label, which is the Label configured in the Kubernetes plugin, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/9838bbb94a31322ce4e9eb4c31b59cc3-0/wm)

In the **Build** step, select **Execute Shell** and enter the following in the text:

```bash
echo "test docker command"
docker info

echo "------------"

echo "test kubectl command"
kubectl get pod
```

as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/cbaeb616f685ed6e66929d64ddcac9f1-0/wm)

Then click Save to complete the project configuration.

First open **Terminal** and type `kubectl get pod -n devops -w` to observe the Slave creation.

Click **Build Now** again, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/66350e1eda86607649f327668c3fdee6-0/wm)

Then in the terminal you can see the entire process of jenkins-slave from creation to deletion, as follows

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/10053ce9cf25c3522b0cfa05b4ad9eee-0/wm)

You can also see the build history in the jenkins panel, as follows

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/ec60430f4fd7d0c9116727bfddfd0f08-0/wm)

Click on a task in the build history and select **Console Output** to see the specific build log, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/b7d2cbc16cde9a1771ca5a0bf19bf6c4-0/wm)

Now, we have finished configuring Kubernetes-based dynamic Slave generation.
