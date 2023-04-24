# Create a Daemonset

Create a DaemonSet to run replicas of the `myapp-pod` on every node in the cluster. Create a file called `/home/labex/project/myapp-daemonset.yaml` with the following contents:

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
          image: nginx
          ports:
            - containerPort: 80
```

This DaemonSet uses the `myapp-pod` as the template for the replicas and sets the `matchLabels` selector to `app: myapp` to ensure that the replicas are created on every node.

Create the DaemonSet using the following command:

```shell
kubectl apply -f /home/labex/project/myapp-daemonset.yaml
```
