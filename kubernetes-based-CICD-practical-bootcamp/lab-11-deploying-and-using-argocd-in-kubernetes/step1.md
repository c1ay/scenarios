## What is GitOps

GitOps is a set of practices for managing infrastructure and application configuration using Git, which refers to an open source version control system. GitOps runs with Git as the single source of truth for declarative infrastructure and applications.

GitOps uses Git pull requests to automatically manage infrastructure provisioning and deployment, and Git repositories contain the full state of the system, so that traces of changes to the system state can be both viewed and audited.

![图片描述](assets/lab-deploying-and-using-argocd-in-kubernetes-0-0.png)

where:

- When the developer pushes the finished code to the git repository, it triggers the CI to create an image and push it to the image repository
- Once the CI is done, you can manually or automatically modify the application configuration and push it to the git repository.
- GitOps compares both the target state and the current state, and if they don't match, it triggers the CD to deploy the new configuration to the cluster.

Compared to traditional CICD, GitOps has the following advantages:

- Git-centric, with Git as the sole source of the application
- Consistent environment, so if you have multiple clusters, you can ensure that each cluster's environment is consistent
- Scalable, with hundreds of clusters that can be scaled to manage hundreds or thousands of containers
- More secure, without the need to grant additional permissions, such as Kubernetes cluster management permissions
