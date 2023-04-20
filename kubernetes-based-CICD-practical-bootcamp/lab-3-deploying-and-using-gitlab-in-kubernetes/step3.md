### Create a Redis persistent store

Redis is primarily used as a cache, as is the entire Gitlab system. Although it's a memory-based database, its data is also stored locally in order to keep the service reliable, whether it's in RDB mode or AOF mode, so for Redis, we need to do a good job of persisting the data when we deploy it for later maintenance.

Create a `redis-pvc.yaml` file in the `/home/shiyanlou/Code/devops/sy-01-2` directory and write the following:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata.
  name: redis-pvc
  namespace: devops
spec.
  accessModes.
    - ReadWriteOnce
  # Specify the OpenEBS sc used here
  storageClassName: openebs-hostpath
  resources.
    requests.
      storage: 5Gi
```

Then use `kubectl apply -f redis-pvc.yaml` to create the PVC, and use `kubectl get pvc -n devops redis-pvc` to check the creation status after the creation is done, the following indicates successful creation.

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/c375ceaadb8382f2dc66f4aa4b124710-0/wm)

> PS: The status of the PVC is Pending because the binding mode of the cluster's StroageClass is WaitForFirstConsumer, in which only the relevant Pod will be created when it uses the corresponding PVC. You can see the detailed configuration of StorageClass by `kubectl get sc openebs-hostpath -oyaml`.
