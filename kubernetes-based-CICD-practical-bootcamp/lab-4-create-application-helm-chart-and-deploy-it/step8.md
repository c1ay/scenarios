## Make Helm Chart

Create a `sy-01-3` folder in the `/home/shiyanlou/Code/devops` directory with the following command:

```bash
mkdir -p /home/shiyanlou/Code/devops/sy-01-3
cd /home/shiyanlou/Code/devops/sy-01-3
```

Then use `helm create` to create a `go-hello-word` chart with the following command:

```bash
helm create go-hello-world
```

After creation, the following folders and files are created:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/953b1c966f0953f090d856c7976f5477-0/wm)

where:

- Chart.yaml: Used to describe the basic information of this Chart, including the name, description information and version.
- values.yaml: stores the values of the variables used in the template files in the templates directory.
- Templates: directory where all yaml template files are stored.
- charts: The directory that holds all the child charts that this chart depends on.
- NOTES.txt: A directory that introduces the Chart help information that will be presented to users after helm install is deployed. For example, how to use the Chart, list the default settings, etc.
- \_helpers.tpl: A place for template helpers, which can be reused throughout the chart.

In fact, this completes the Chart and creates an Nginx Chart by default, isn't that easy?

However, in practice, adjustments will definitely be made on top of this, and we need to make some adjustments here as well. In `go-hello-world`, the application port is `8080` and the health detection interface is `/health`. For convenience, these fields are configured as variables here to facilitate adaptation to other types of applications.

- Modify `go-hello-world/templates/deployment.yaml` with the following changes:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/086ca03d13bd4ca8f2964a6e046daabe-0/wm)

- Modify `go-hello-world/values.yaml` to read as follows

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/c18a1d5c2a49516bdd71c4372435b642-0/wm)

At this point, the Helm Chart modification is complete and can be saved to the code repository under the `go-hello-world` project.

First pull `go-hello-world` into `/home/shiyanlou/Code` using `git clone` with the following command:

```bash
cd /home/shiyanlou/Code
git clone http://10.111.127.141:30180/devops/go-hello-world.git
```

> PS: The code address is filled in according to your actual situation.

Then create a `deploy/charts` folder in the code directory and copy the Helm Chart you made above into the code directory with the following command:

```bash
cd /home/shiyanlou/Code/go-hello-world
mkdir deploy/charts -p
cd deploy/charts
cp -r /home/shiyanlou/Code/devops/sy-01-3/go-hello-world/* .
```

At this point the Helm Chart is copied to the code directory and we push the code to the remote repository with the following command:

```bash
cd /home/shiyanlou/Code/go-hello-world
git config --global user.email "joker@devops.com"
git config --global user.name "joker"
git add .
git commit -m "add deploy helm chart"
git push
```

> PS: Whether you're pushing or pulling code, you'll need to enter your username and password

Then you can see the new Helm Chart in the code repository.
