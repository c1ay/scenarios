### Create a Gitlab persistent store

Create a `gitlab-pvc.yaml` file in the `/home/shiyanlou/Code/devops/sy-01-2` directory and write the following:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata.
  name: gitlab-pvc
  namespace: devops
spec.
  accessModes.
    - ReadWriteOnce
  storageClassName: openebs-hostpath
  resources.
    requests.
      storage: 5Gi
```

Then use `kubectl apply -f gitlab-pvc.yaml` to create the PVC and use `kubectl get pvc -n devops gitlab-pvc` to see the result of the creation, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/5b6580c2aa64ff719b053bf326d6dc0e-0/wm)
