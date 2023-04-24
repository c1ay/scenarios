### Create PostgreSQL application

Create a `postgresql-deploy.yaml` file in the `/home/shiyanlou/Code/devops/sy-01-2` directory and write the following:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata.
  name: postgresql
  namespace: devops
  labels.
    name: postgresql
spec.
  replicas: 1
  selector.
    matchLabels.
      name: postgresql
  template.
    metadata.
      name: postgresql
      labels.
        name: postgresql
    spec.
      containers.
        - name: postgresql
          image: sameersbn/postgresql:10
          imagePullPolicy: IfNotPresent
          env.
            - name: DB_USER
              value: gitlab
            - name: DB_PASS
              value: passw0rd
            - name: DB_NAME
              value: gitlab_production
            - name: DB_EXTENSION
              value: pg_trgm
          ports.
            - name: postgres
              containerPort: 5432
          volumeMounts.
            - mountPath: /var/lib/postgresql
              name: data
          livenessProbe.
            exec.
              command.
                - pg_isready
                - -h
                - localhost
                - -U
                - postgres
            initialDelaySeconds: 30
            timeoutSeconds: 5
          readinessProbe.
            exec.
              command.
                - pg_isready
                - -h
                - localhost
                - -U
                - postgres
            initialDelaySeconds: 5
            timeoutSeconds: 1
      volumes.
        - name: data
          persistentVolumeClaim.
            claimName: postgresql-pvc
```

Then use `kubectl apply -f postgresql-deploy.yaml` to create PostgreSQL, and then use `kubectl get po -n devops | grep postgresql` to check the creation status, only when the Pod status becomes running, it means the creation is successful. The status of the Pod is running, as follows:

![图片描述](assets/lab-deploying-and-using-gitlab-in-kubernetes-7-0.png)
