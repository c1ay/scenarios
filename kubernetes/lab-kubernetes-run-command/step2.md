# Creating a Job

In this step, we will create a job using the `kubectl run` command. Here are the steps:

1. Run the following command to create a job that runs a container with the `busybox` image and performs a simple task, such as printing a message:

```bash
kubectl run job1 --image=busybox --restart=OnFailure -- echo "Hello from Job 1"
```

2. Verify that the job has been created successfully by checking the status using the following command:

```bash
kubectl get pod job1
```
