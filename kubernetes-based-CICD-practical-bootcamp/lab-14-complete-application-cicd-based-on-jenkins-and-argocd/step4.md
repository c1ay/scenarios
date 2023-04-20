## Test

Before testing, change the Tag generation criteria for `tools.groovy` in `jenkins-sharelibrary`, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/00e94085e214f24a7c1feca8ba8874f2-0/wm)

Add a `_devops` string to the end of it. If it's all numbers, it will become a long int when you push it to Gitlab, changing the Tag itself.

Then you can go to the dev branch of the `go-hello-world` project, make some random changes, and see if the pipeline on Jenkins is working properly:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/9fef0a0f3b8b10c0d80369ac3920f623-0/wm)

Observe that the application deployment on Argocd is also normal, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/d9c746f61e82a3f8a9207da490f4ea05-0/wm)

> PS: On Argocd, we see that the application keeps spinning, because we have Ingress and the IP of the status state of this Ingress is empty, Argocd checksum does not pass, but it does not affect the usage.
