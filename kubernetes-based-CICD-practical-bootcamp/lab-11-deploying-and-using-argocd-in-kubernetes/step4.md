## Access Argocd

After deployment, you can use `argocd-server` to access the UI interface and use `kubectl get serivce -n argocd` to check the service status as follows

![图片描述](assets/lab-deploying-and-using-argocd-in-kubernetes-3-0.png)

However, the services in the above diagram are of the ClusterIP type, which cannot be accessed directly from outside, and can be accessed in two ways:

- Change the Service type to NodePort
- Add an Ingress

For convenience, here we use NodePort directly for access.

Access the Service edit interface via `kubectl edit service -n argocd argocd-server`, as follows:

![图片描述](assets/lab-deploying-and-using-argocd-in-kubernetes-3-1.png)

Then change the Type type to `NodePort`, save and exit.

Use `kubectl get service -n argocd argocd-server` to see the NodePort, as follows:

![图片描述](assets/lab-deploying-and-using-argocd-in-kubernetes-3-2.png)

The diagram shows a NodePort of `30888`, which we can then access using `http://10.111.127.141:30888`, as follows:

![图片描述](assets/lab-deploying-and-using-argocd-in-kubernetes-3-3.png)

The default username is `admin` and the password is stored in `argocd-initial-admin-secret`, which can be viewed with the following command:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
```

as follows:

![图片描述](assets/lab-deploying-and-using-argocd-in-kubernetes-3-4.png)

Then, after logging in with your username and password, you will enter the following screen:

![图片描述](assets/lab-deploying-and-using-argocd-in-kubernetes-3-5.png)
