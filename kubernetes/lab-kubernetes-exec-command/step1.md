# Executing a Command in a Container

In this step, you will learn how to execute a command in a container running in a pod.

1. Start by creating a deployment with one replica and an Nginx container:

   ```bash
   kubectl create deployment nginx --image=nginx --replicas=1
   ```

2. Wait for the pod to become ready:

   ```bash
   kubectl wait --for=condition=Ready pod -l app=nginx
   ```

3. Use the `kubectl exec` command to execute a command inside the Nginx container:

   ```bash
   kubectl exec nginx -v < pod_name > --
   ```

   Replace `<pod_name>` with the name of the pod created in step 1, and you can get the `<pod_name>` with the `kubectl get pod -l app=nginx` command.
