### Application deployment

Create a `test-argocd` project on Gitlab, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/7ebb6286cb120b5a192b66d4b5739217-0/wm)

Then add a new `deployment.yaml` file to the `test-argocd` repository and write the following:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata.
  name: myapp
spec.
  selector.
    matchLabels.
      app: myapp
  replicas: 2
  template.
    metadata.
      labels.
        app: myapp
    spec.
      containers.
        - name: myapp
          image: nginx:latest
          ports.
            - containerPort: 80
```

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/16d79e4c4ccaaad9533048e82abc45cd-0/wm)

Add another `service.yaml` file and enter the following:

```yaml
apiVersion: v1
kind: Service
metadata.
  name: myapp
spec.
  selector.
    app: myapp
  ports.
    - port: 80
      protocol: TCP
      targetPort: 80
```

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/6232a85c2fbadc53391101669ac71b1e-0/wm)

Finally, we create an argo-application.yaml file in `/home/shiyanlou/Code/devops/sy-03-1` and enter the following:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata.
  name: myapp
  namespace: argocd
spec.
  project: default

  source.
    repoURL: http://10.111.127.141:30180/devops/test-argocd.git
    targetRevision: HEAD
    path: .
  destination.
    server: https://kubernetes.default.svc
    namespace: default

  syncPolicy.
    syncOptions.
      - CreateNamespace=true

    automated.
      selfHeal: true
      prune: true
```

At this point, if you use `kubectl apply -f argo-application.yaml` to create the repository directly, you will get an error because our Git repository is private and you need to be logged in to authenticate.

In the UI, click `Settings` and select `Repositories` to get to the following screen:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/697b5d28428db7e3d9d162652fcdf568-0/wm)

Then click `CONNECT REPO USING HTTPS` and enter the repository information as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/5e5a9a4a450407a1631d962d16288a1e-0/wm)

Then click `CONNECT` above to create, as follows to indicate a successful connection:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/3b0b271f720ab2d1f8205468ebfbc087-0/wm)

Now, let's execute `kubectl apply -f argo-application.yaml` again to create the application, and after creating it, you can see the application in the UI interface as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/c69126bf4a2a3ca1bf7cb2fbb88058a5-0/wm)

Click inside to see more detailed information, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/610225a58df9c60ccca3ffbd678c8b7e-0/wm)
