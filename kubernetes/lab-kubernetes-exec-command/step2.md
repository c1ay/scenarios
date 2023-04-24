# Executing a Command in a Specific Container

In this step, you will learn how to execute a command in a specific container running in a pod with multiple containers.

1. Create a pod with two containers: Nginx and BusyBox:

   ```bash
   cat << EOF | kubectl apply -f -
   apiVersion: v1
   kind: Pod
   metadata:
     name: nginx-busybox
   spec:
     containers:
     - name: nginx
       image: nginx
     - name: busybox
       image: busybox
       command:
         - sleep
         - "3600"
   EOF
   ```

2. Wait for the pod to become ready:

   ```bash
   kubectl wait --for=condition=Ready pod nginx-busybox
   ```

3. Use the `kubectl exec` command to execute a command inside the BusyBox container:

   ```bash
   kubectl exec nginx-busybox -c busybox -- ls /bin
   ```
