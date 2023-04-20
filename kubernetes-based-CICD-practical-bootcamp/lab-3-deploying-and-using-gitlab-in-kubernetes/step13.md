### Creating a Gitlab Service

Create a `gitlab-svc.yaml` file in the `/home/shiyanlou/Code/devops/sy-01-2` directory, and write the following:

```yaml
apiVersion: v1
kind: Service
metadata.
  name: gitlab
  namespace: devops
  labels.
    name: gitlab
spec.
  ports.
    - name: http
      port: 80
      targetPort: http
      nodePort: 30180
    - name: ssh
      port: 22
      targetPort: ssh
      nodePort: 30022
  selector.
    name: gitlab
  type: NodePort
```

> PS: Gitlab's Service uses NodePort here because we need to access it from the outside.

Then use `kubectl apply -f gitlab-svc.yaml` to create the Service, and then use `kubectl get svc -n devops gitlab` to see how the Service was created, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/3a645d8170308f6ab75a23f3f02f149e-0/wm)

And you can use `kubectl describe svc -n devops gitlab` to see the details of the Service, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/648d9e9e1a357cc4d4933e0bf7ebff9f-0/wm)

At this point, Gitlab deployment is complete.
