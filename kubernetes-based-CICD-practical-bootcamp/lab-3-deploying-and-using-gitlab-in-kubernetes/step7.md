### Creating a PostgreSQL persistent store

Create a `postgresql-pvc.yaml` file in the `/home/shiyanlou/Code/devops/sy-01-2` directory, and write the following:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata.
  name: postgresql-pvc
  namespace: devops
spec.
  accessModes.
    - ReadWriteOnce
  storageClassName: openebs-hostpath
  resources.
    requests.
      storage: 5Gi
```

Then use `kubectl apply -f postgresql-pvc.yam`l to create the PVC, and use `kubectl get pvc -n devops postgresql-pvc` to check the PVC creation status after it is done.

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/b7533d7f8c9f8bcc6174d9da89fd3155-0/wm)
