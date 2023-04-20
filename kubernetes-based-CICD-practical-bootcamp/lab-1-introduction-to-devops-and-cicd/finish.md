## What are the common CICD processes?

Nowadays, very few companies do manual version updates and restart applications, even the smallest companies have a CICD process.

(1) host mode: this process is mainly deployed on bare metal applications

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/45ef2d8e191572a3bc79d176125dc842-0/wm)

This model is mainly done through Jenkins for continuous integration and then through Ansible automation tools for continuous delivery.

(2) Container mode: This process is mainly to deploy the application to Kubernetes

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/a7eccb9755611833f6a92ff56678153a-0/wm)

(3) Using GitOps

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/249a342a0a5946385b7a6dc118517e07-0/wm)

The above CI processes are the most basic ones, but you can add your own processes to them, such as automated testing, code quality testing, product security testing, and so on. This column focuses on the third type: using Jenkins+GitOps to achieve continuous delivery.
