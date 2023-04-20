## Deploy Argocd

Argocd can be deployed in two ways: the highly available way and the non-highly available way. For production, it is recommended to use the highly available deployment method. For simple trial and testing, you can choose the non-high availability method, which can be viewed at `https://github.com/argoproj/argo-cd/tree/master/manifests`.

Here we use the non-high availability deployment method.

(1) Create namespace

```bash
kubectl create namespace argocd
```

(2) Deploy the service

```bash
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

If the network is bad, try the following installation:

```bash
kubectl apply -n argocd -f https://gitee.com/coolops/kubernetes-devops-course/raw/master/argocd/install.yaml
```

After deployment, use `kubectl get pod -n argocd` to see the deployment status as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/09a202871856641eb20deeba7173409c-0/wm)

(3) Create a directory to save user configuration files

```bash
mkdir -p /home/shiyanlou/Code/devops/sy-03-1
```
