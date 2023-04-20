### Configure Webhook to speed up Argocd configuration updates

Of course, we're actually configuring automatic synchronization, which means that after you update your Gitlab image, Argocd will automatically pull the configuration and update it, but not in real time.

To eliminate polling latency, you can configure the API server to receive Webhook events. argo CD supports Git Webhook notifications from GitHub, GitLab, Bitbucket, Bitbucket Server, and Gogs, and we're focusing on configuring Gitlab here.

#### modifies argocd-secret to add a Gitlab webhook token

Use `kubectl edit secret argocd-secret -n argocd` to open the configuration file and add the following code:

```yaml
stringData.
  webhook.gitlab.secret: test-argocd-token
```

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/40b0380d09f1dd0e28f70fa4b35660a6-0/wm)

Click save and save it to argocd-secret, and use `kubectl describe secret argocd-secret -n argocd` to see it as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/10c2d8fd358048c24388722d22dbd8a8-0/wm)

Then on Gitlab, select `settings` -> `integrations` to configure the webhook, as follows

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/ccb06642c6fb17045ef9ff02166ef5d9-0/wm)

Since the cluster internal certificate is an invalid certificate, remove the Enabled SSL as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/0b74e8f04847aeb79f549671646967e2-0/wm)

Then you can test the update, and you can see that Argocd will start executing the update as soon as you commit it in Gitlab, so you can test it yourself.
