### Installing Aro rollouts

Argo rollouts is divided into a server-side and a client-side installation, where the server side is a series of custom CRDs and Controllers, and the client side is a kubectl plugin that can be used to view and manage the Argo rollouts application.

First create the `argo-rollouts` namespace with the following command:

```bash
kubectl create namespace argo-rollouts
```

Install directly using the following command:

```bash
kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/download/v1.2.2/install.yaml
```

After the installation is complete, use `kubectl get pod -n argo-rollouts` to see how the pod is starting up, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/3cc88eb43140d04d56d74c2954344824-0/wm)

After the Controller installation is complete, now install the kubectl plugin.

Select the corresponding version directly from `https://github.com/argoproj/argo-rollouts/releases`, for example, I have `v1.2.2` here, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/725e3409415cb5467ad381822ccc24e1-0/wm)

Then select the corresponding version to download as follows:

```bash
curl -LO https://github.com/argoproj/argo-rollouts/releases/download/v1.2.2/kubectl-argo-rollouts-linux-amd64
chmod +x . /kubectl-argo-rollouts-linux-amd64
sudo mv . /kubectl-argo-rollouts-linux-amd64 /usr/local/bin/kubectl-argo-rollouts
```

Then use `kubectl argo rollouts version` to see if it succeeds, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/ef8a6efae439277c60a39170153d3114-0/wm)

This completes the installation steps.
