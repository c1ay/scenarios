### Application Updates

Now, to update the application, instead of changing the image on Argocd, you only need to change the image address of `deployment.yaml` in the `test-argocd` repository, as follows: we update the image from `nginx:latest` to `nginx:1.8`:

![图片描述](assets/lab-deploying-and-using-argocd-in-kubernetes-7-0.png)

Then click `sync` on Argocd as follows:

![图片描述](assets/lab-deploying-and-using-argocd-in-kubernetes-7-1.png)

This will update the application to the latest image.

We can check to see if the commit on Gitlab matches the commit synced on argocd, as follows:

![图片描述](assets/lab-deploying-and-using-argocd-in-kubernetes-7-2.png)

![图片描述](assets/lab-deploying-and-using-argocd-in-kubernetes-7-3.png)
