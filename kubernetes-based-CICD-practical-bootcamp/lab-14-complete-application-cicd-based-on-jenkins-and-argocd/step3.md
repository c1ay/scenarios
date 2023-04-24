## Deploy the application on Argocd

First, add a repository to Argocd in `settings` -> `repositories`, as follows:

![图片描述](assets/lab-complete-application-cicd-based-on-jenkins-and-argocd-2-0.png)

Configure `argocd-charts` code repository information as follows:

![图片描述](assets/lab-complete-application-cicd-based-on-jenkins-and-argocd-2-1.png)

Then create the application, which we do directly on the Argocd UI.

- Click on `New APP` to create the application

![图片描述](assets/lab-complete-application-cicd-based-on-jenkins-and-argocd-2-2.png)

- Enter the configuration information

![图片描述](assets/lab-complete-application-cicd-based-on-jenkins-and-argocd-2-3.png)

![图片描述](assets/lab-complete-application-cicd-based-on-jenkins-and-argocd-2-4.png)

![图片描述](assets/lab-complete-application-cicd-based-on-jenkins-and-argocd-2-5.png)

Then click Save.
