## Change password

The initial password is complex and not suitable for remembering, so it may be necessary to change it.

There is no place to change the password in the UI interface, so if you want to change the password, you can only do it through the client.

You can choose the appropriate client from the `https://github.com/argoproj/argo-cd/releases` page, or if the network is better, you can install it directly using the following command:

```bash
wget https://github.com/argoproj/argo-cd/releases/download/v2.4.9/argocd-linux-amd64
chmod +x argocd-linux-amd64
sudo mv argocd-linux-amd64 /usr/local/bin/argocd
```

If the network conditions are not good, you can use the following command for installation:

```bash
wget https://gitee.com/coolops/go-hello-world/releases/download/v2.4.9/argocd-linux-amd64.zip
unzip argocd-linux-amd64.zip
chmod +x argocd-linux-amd64
sudo mv argocd-linux-amd64 /usr/local/bin/argocd
```

After the installation is complete use `argocd version` to view the information as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/a141d73093af0b66ce1319525c237145-0/wm)

We found that the query for Argocd-Server failed because we need to log in, so we used `argocd login 10.111.127.141:30888` to log in, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/c7a96bd09defc82474c76f930b6b6ea0-0/wm)

Once logged in successfully, you can query the information using `argocd version` as follows

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/d0c1240d8892b63bdf3017f6e38bbac0-0/wm)

Now, we can use `argocd account update-password --account admin --current-password xxxx --new-password xxxx` to change the password, for example, I change it to `Argocd@123456` here, the full command is as follows

```bash
argocd account update-password --account admin --current-password 04Y0P54LzoxGEYno --new-password Argocd@123456
```

The output of the successful modification is as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/5295896ee6fd67d2611dc3ef1eae5861-0/wm)

Then the UI interface can be re-logged in with the new password.
