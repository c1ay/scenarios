# Expose a Deployment

In this step, we will expose a deployment using the `expose` command. We will create a deployment with one replica, and then expose it as a service.

1. Create a new deployment named `hello-world` with the `nginx` image and one replica:

   ```bash
   kubectl create deployment hello-world --image=nginx --replicas=1
   ```

2. Expose the `hello-world` deployment as a service named `hello-service` on port 80:

   ```bash
   kubectl expose deployment hello-world --name=hello-service --port=80 --target-port=80 --type=NodePort
   ```

   The `--target-port` flag specifies the port that the container is listening on, while the `--port` flag specifies the port that the service will be available on. The `--type` flag specifies the type of service, in this case, a NodePort service.

   The `NodePort` type of service allows access to the service from a specific port on each node in the cluster. The port is assigned automatically by Kubernetes from a range of ports configured in the cluster.

3. Get the details of the `hello-service` service:

   ```bash
   kubectl get services hello-service
   ```

   This command will show the details of the `hello-service` service, including the `PORT(S)` on which the service is listening.
