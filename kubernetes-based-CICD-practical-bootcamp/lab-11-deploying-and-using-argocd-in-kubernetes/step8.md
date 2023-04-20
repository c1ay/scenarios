### Application Updates

Now, to update the application, instead of changing the image on Argocd, you only need to change the image address of `deployment.yaml` in the `test-argocd` repository, as follows: we update the image from `nginx:latest` to `nginx:1.8`:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/e1796cab14da99f331355355f8d6f34c-0/wm)

Then click `sync` on Argocd as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/83fd548b4b6edc27f4d2b2ccbaf294e6-0/wm)

This will update the application to the latest image.

We can see if the commit on Gitlab matches the commit synced on argocd, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/16058ce892f78044cd5443c75e397acd-0/wm)

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/69a2d63c260a302f75b2a6ca3b557ae0-0/wm)
