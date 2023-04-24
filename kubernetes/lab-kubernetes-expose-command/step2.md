# Access the Exposed Service

In this step, we will access the service that we exposed in the previous step using `curl`.

1. Get the IP address of any node in the cluster:

   ```bash
   kubectl get nodes -o wide
   ```

2. Use `curl` to access the `hello-service` service on the IP address and NodePort that Kubernetes assigned to the service:

   ```bash
   curl <NODE_IP>:<NODE_PORT>
   ```

   Replace `<NODE_IP>` and `<NODE_PORT>` with the IP address and NodePort that Kubernetes assigned to the `hello-service` service.

   If everything is configured correctly, you should see the default `nginx` welcome page.
