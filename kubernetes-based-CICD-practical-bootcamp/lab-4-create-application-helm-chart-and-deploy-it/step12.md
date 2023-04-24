### Application rollback

If the release does not work as expected, you can use helm rollback to roll back to the previous version.

If rolling back directly to the previous version, use the following command:

```bash
helm rollback nginx
```

To roll back to a specified version, use the following command:

```bash
helm rollback nginx 1
```

After the rollback, you can use `helm history RELEASE_NAME` to view the history version as follows:

![图片描述](assets/lab-create-application-helm-chart-and-deploy-it-11-0.png)
