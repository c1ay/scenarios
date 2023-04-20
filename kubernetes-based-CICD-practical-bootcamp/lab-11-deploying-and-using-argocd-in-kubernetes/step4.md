## Access Argocd

After deployment, you can use `argocd-server` to access the UI interface and use `kubectl get serivce -n argocd` to view the service status as follows

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/ddaf6c356afa143536d4135b0fce2133-0/wm)

However, the services in the above diagram are of the ClusterIP type, which cannot be accessed directly from outside, and can be accessed in two ways:

- Change the Service type to NodePort
- Add an Ingress

For convenience, here we use NodePort directly for access.

Access the Service edit interface via `kubectl edit service -n argocd argocd-server`, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/7586d8cb006407d84cddcbd8eece669f-0/wm)

Then change the Type type to `NodePort`, save and exit.

Use `kubectl get service -n argocd argocd-server` to see the NodePort, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/ae623c418026a76778ba50710f33523c-0/wm)

The diagram shows a NodePort of `30888`, which we can then access using `http://10.111.127.141:30888` as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/c76918651ee23fd34f7a41d84f108228-0/wm)

The default username is `admin` and the password is stored in `argocd-initial-admin-secret`, which can be viewed with the following command:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
```

as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/6b81ef5dbd40ce0107a87fac525f5a66-0/wm)

Then, after logging in with your username and password, you will enter the following screen:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/56213484111f725ab341ad64d1217498-0/wm)
