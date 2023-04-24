### Application rollback

The rollback is also based on Git, and we can look at the Git History as follows:

![图片描述](assets/lab-deploying-and-using-argocd-in-kubernetes-8-0.png)

Then you can find the last commit we committed and click on it:

![图片描述](assets/lab-deploying-and-using-argocd-in-kubernetes-8-1.png)

Find `options` and select `revert`, which will create a new Merage Request, as follows:

![图片描述](assets/lab-deploying-and-using-argocd-in-kubernetes-8-2.png)

Clicking submit will take you to the `merge` page, as follows:

![图片描述](assets/lab-deploying-and-using-argocd-in-kubernetes-8-3.png)

Then click `merge` to roll back the image, as follows:

![图片描述](assets/lab-deploying-and-using-argocd-in-kubernetes-8-4.png)

Finally, just go to Argocd and click sync.
