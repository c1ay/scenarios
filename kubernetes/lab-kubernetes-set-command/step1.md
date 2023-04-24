# Modify Image of a Deployment

In this step, we will use the `set` command to modify the image of an existing deployment.

1. Create a new deployment named `hello-world` with the `nginx` image and one replica:

   ```bash
   kubectl create deployment hello-world --image=nginx --replicas=1
   ```

2. Use the `set` command to update the `nginx` container with the image `nginx:1.19.10`, you would run the following command:

   ```bash
   kubectl set image deployment/hello-world nginx=nginx:1.19.10
   ```

   Note that this command will only update the specified container's image. If you have multiple containers in your deployment, you will need to run this command for each container.

3. Verify that the image was updated to the deployment by running the following command:

   ```bash
   kubectl get deployment hello-world -o jsonpath='{.spec.template.spec.containers[0].image}'
   ```

   This command will show the image of the `hello-world` deployment.
