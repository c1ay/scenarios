## Introduction to the experiment

We have completed Jenkins and Argocd-centric continuous delivery in the previous section, but now the whole application release is still just a rolling update, so how can we do a grayscale release?

The straightforward way is to manually maintain another set of applications, including Ingress, Service and Deployment, and then finish the grayscale release by switching.

#### knowledge points

- argo rollouts
- argocd
- jenkins pipeline
- helm charts
