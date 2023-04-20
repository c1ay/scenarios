### Creating a Redis service

Create a `redis-deploy.yaml` file in the `/home/shiyanlou/Code/devops/sy-01-2` directory and write the following:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata.
  name: redis
  namespace: devops
  labels.
    name: redis
spec.
  replicas: 1
  selector.
    matchLabels.
      name: redis
  template.
    metadata.
      name: redis
      labels.
        name: redis
    spec.
      containers.
        - name: redis
          image: sameersbn/redis
          imagePullPolicy: IfNotPresent
          ports.
            - name: redis
              containerPort: 6379
          volumeMounts.
            - mountPath: /var/lib/redis
              name: data
          livenessProbe.
            exec.
              command.
                - redis-cli
                - ping
            initialDelaySeconds: 30
            timeoutSeconds: 5
          readinessProbe.
            exec.
              command.
                - redis-cli
                - ping
            initialDelaySeconds: 5
            timeoutSeconds: 1
      volumes.
        - name: data
          persistentVolumeClaim.
            claimName: redis-pvc
```

Use `kubectl apply -f redis-deploy.yaml` to deploy Redis, and `kubectl get po -n devops | grep redis` to check the Redis deployment status, and when the status changes to running, the deployment is successful, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/6910246e42e39479719641b445cbe61e-0/wm)
