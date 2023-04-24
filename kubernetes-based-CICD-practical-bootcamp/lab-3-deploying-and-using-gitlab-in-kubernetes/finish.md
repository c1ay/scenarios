## Experiment Summary

The entire Gitlab project consists of three main components: Redis, PostgreSQL, and Gitlab. The process of deploying each component is pretty much the same: you create a storage volume PVC, then use Deployment to deploy the service, and finally use Service for application access. In a formal environment, if you want to deploy stateful services to Kubernetes, it is recommended to use StatefulSet or Operator to better manage stateful applications.

Gitlab is a code repository that holds the source code for our entire experiment, including application code, YAML manifests, and so on. So please remember the address and username and password, as they will be used from time to time.
