# Creating a Deployment

In this step, we will create a simple deployment using the `kubectl run` command. Here are the steps:

1. Run the following command to create a pod with a single replica running the `nginx` container image:

```bash
kubectl run nginx-pod --image=nginx
```

2. Verify that the pod has been created successfully by checking the status using the following command:

```bash
kubectl get pods
```
