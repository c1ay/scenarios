### Create PostgreSQL Service

Create a `postgresql-svc.yaml` file in the `/home/shiyanlou/Code/devops/sy-01-2` directory and write the following:

```yaml
apiVersion: v1
kind: Service
metadata.
  name: postgresql
  namespace: devops
  labels.
    name: postgresql
spec.
  ports.
    - name: postgres
      port: 5432
      targetPort: postgres
  selector.
    name: postgresql
```

Then use `kubectl apply -f postgresql-svc.yaml` to create the Service, and then use `kubectl get svc -n devops postgresql` to view the creation, as follows:

![图片描述](assets/lab-deploying-and-using-gitlab-in-kubernetes-8-0.png)

And you can use `kubectl describe svc -n devops postgresql` to see the details of the Service, as follows

![图片描述](assets/lab-deploying-and-using-gitlab-in-kubernetes-8-1.png)

At this point, the PostgreSQL deployment is complete.
