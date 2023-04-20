### Client operations

Now, we are going to try to Pull/Push the image to the Harbor repository. First we need to log into Harbor with the following command:

```bash
docker login http://10.111.127.141:30002
```

When we enter the username/password: `admin/Harbor12345`, we will find that we cannot log in, and the error will be as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/ed1300a8541869cb1f0421600df9697b-0/wm)

This is due to the fact that the default docker registry uses https, while the current Harbor uses http. We need to change the Docker configuration by using `sudo vim /etc/docker/daemon.json` and inserting the following in it:

```json
  "insecure-registries": ["http://10.111.127.141:30002"]
```

Modified as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/4648d61004a3c901a95f74dc3c3b35c4-0/wm)

Then reload the docker configuration file with the following command:

```bash
sudo systemctl daemon-reload
sudo systemctl reload docker
```

> PS: If the login still fails with `sudo systemctl reload docker`, you need to restart Docker with `sudo systemctl restart docker`, which will cause the Kubernetes cluster to rebuild, which will take longer.

Now we can continue logging in using `docker login http://10.111.127.141:30002`, which works as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/7fff8728c11bce8aef49d13fe493b2e4-0/wm)

#### pushing the image to the Harbor repository

Our local image of `nginx:1.8` now exists, as follows:
![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/63725ef57263e6a33759032491398aec-0/wm)

This Nginx is pulled from Dockerhub, so to push it to the private Harbor, we need to change the image name with the following command:

```bash
docker tag nginx:1.8 10.111.127.141:30002/dev/nginx:1.8
```

Then use the `docker push` command to push the image to Harbor with the following command:

```bash
docker push 10.111.127.141:30002/dev/nginx:1.8
```

The output is as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/29443c86e5c7fa7f7f0125cb78412085-0/wm)

The pushed up image can be viewed on Harbor as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/36c5d2ff27301adc1cdd0daf4e635b38-0/wm)

#### pulls mirrors

The prerequisite for pulling a mirror is also to be logged into Harbor, and since we are already logged in, we can pull it directly using the command here, as follows.

```bash
docker pull 10.111.127.141:30002/dev/nginx:1.8
```

This completes the basic operation of Harbor.
