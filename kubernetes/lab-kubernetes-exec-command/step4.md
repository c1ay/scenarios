# Executing a Command with Environment Variables

In this step, you will learn how to execute a command with environment variables inside a container.

1. Create a deployment with one replica and an Nginx container with an environment variable:

   ```bash
   kubectl run nginx-env --image=nginx --env="MY_VAR=my-value"
   ```

2. Wait for the pod to become ready:

   ```bash
   kubectl wait --for=condition=Ready pod -l run=nginx-env
   ```

3. Use the `kubectl exec` command to execute a command inside the Nginx container that outputs the environment variable:

   ```bash
   kubectl exec nginx-env -- sh -c 'echo $MY_VAR'
   ```

   Replace nginx-env with the name of the pod created in step 1.
