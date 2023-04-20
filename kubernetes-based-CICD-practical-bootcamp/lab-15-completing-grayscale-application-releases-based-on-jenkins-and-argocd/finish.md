## Experiment Summary

At this point, our Jenkins+Argo rollouts+Argocd-based continuous delivery is complete. First, let's review the whole process:

- First, we modified Helm Charts to work with Argo rollouts' CRD for application management.
- Secondly, we modified the pipeline by removing the automatic triggering of the pipeline and replacing it with manual selection of branches for release.
- Finally, we verified the entire process, from build to grayscale deployment to full update, to ensure that each step was working properly

In fact, whether it is the common rolling update, or grayscale release, we can transform based on these templates, in practice, you can handle at your discretion, the flexibility is still relatively large.
