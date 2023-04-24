# Modify Resources of a Deployment

In this step, we will use the kubectl set command to modify resources (CPU and memory limits/requests) of a Kubernetes Deployment.

1. Use the `set` command to set the CPU and memory limits to `1 CPU` and `512Mi` respectively, and the CPU and memory requests to `500m CPU` and `256Mi` respectively, run the following command:

   ```bash
   kubectl set resources deployment/hello-world --limits=cpu=1,memory=512Mi --requests=cpu=500m,memory=256Mi
   ```

2. Verify that the limits were changed to `1 CPU` and `512Mi` and the requests were changed to `500m CPU` and `256Mi` respectively.

   ```bash
   kubectl describe deployment hello-world
   ```
