# Executing a Command with a Tty

In this step, you will learn how to execute a command with a tty in a container.

1. Use the `kubectl exec` command with the `-it` options to execute a command with a tty:

   ```bash
   kubectl exec -it nginx-busybox -- /bin/sh
   ```

2. Once inside the container shell, run a command:

   ```bash
   echo "Hello, world!"
   ```

3. Exit the container shell:

   ```bash
   exit
   ```
