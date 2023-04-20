### Deploying the application

Deploying an application with Helm is very simple, just use `helm install`, and it can take different parameters, if you don't know how to use it, you can use `helm install -h` to see the help documentation.

Here we deploy the Nginx service, version 1.8, with the following command:

```bash
cd /home/shiyanlou/Code/devops/sy-01-3/
helm install nginx --set image.repository=nginx --set image.tag=1.8 go-hello-world/
```

After the command is executed, the output is as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/5c9a43f8ccf61ee9880f665b51d3aca5-0/wm)

Use `kubectl get pod` to see if the `nignx` service is started properly, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/075967d998f3e31f7d8af82f180d654a-0/wm)

Use `helm list` to see the deployed releases in the cluster, followed by the namespace if it is not under the `default` namespace, for example: `helm list -n kube-system`.

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/ab974e848c653a5a88ae4f0c52ac6f50-0/wm)

where `REVISION` is the current version.
