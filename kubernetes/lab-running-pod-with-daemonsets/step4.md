# Update the Daemonset

Update the DaemonSet to change the image used by the `myapp-container`. Create a file called `/home/labex/project/myapp-daemonsett-update.yaml` with the following contents:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: myapp-daemonset
spec:
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: myapp-container
          image: busybox
          command: ["sleep", "3600"]
```

This updated DaemonSet changes the image used by the `myapp-container` to `busybox` and sets the command to `sleep 3600`.

Update the DaemonSet using the following command:

```shell
kubectl apply -f /home/labex/project/myapp-daemonset-update.yaml
```

Verify that the DaemonSet has been updated and that replicas of the `myapp-pod` are running with the new image. Use the following command to list the pods created by the DaemonSet:

```shell
kubectl get pods -l app=myapp
```

You should see new pods created with the updated image.
