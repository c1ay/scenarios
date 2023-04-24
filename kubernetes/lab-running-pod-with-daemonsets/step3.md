# Verify the Daemonset

Verify that the DaemonSet has been created and that replicas of the `myapp-pod` are running on every node. Use the following command to list the nodes in the cluster:

```shell
kubectl get nodes
```

Use the following command to list the pods created by the DaemonSet:

```shell
kubectl get pods -l app=myapp
```

You should see one pod for each node in the cluster.
