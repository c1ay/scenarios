### Deploying Gitlab Applications

Create a `gitlab-deploy.yaml` file in the `/home/shiyanlou/Code/devops/sy-01-2` directory and write the following:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata.
  name: gitlab
  namespace: devops
  labels.
    name: gitlab
spec.
  replicas: 1
  selector.
    matchLabels.
      name: gitlab
  template.
    metadata.
      name: gitlab
      labels.
        name: gitlab
    spec.
      containers.
        - name: gitlab
          image: sameersbn/gitlab:11.8.1
          imagePullPolicy: IfNotPresent
          env.
            - name: TZ
              value: Asia/Shanghai
            - name: GITLAB_TIMEZONE
              value: Beijing
            - name: GITLAB_SECRETS_DB_KEY_BASE
              value: long-and-random-alpha-numeric-string
            - name: GITLAB_SECRETS_SECRET_KEY_BASE
              value: long-and-random-alpha-numeric-string
            - name: GITLAB_SECRETS_OTP_KEY_BASE
              value: long-and-random-alpha-numeric-string
            - name: GITLAB_ROOT_PASSWORD
              value: admin321
            - name: GITLAB_ROOT_EMAIL
              value: devops@163.com
            - name: GITLAB_HOST
              value: 10.111.127.141
            - name: GITLAB_PORT
              value: "30180"
            - name: GITLAB_SSH_PORT
              value: "30022"
            - name: GITLAB_NOTIFY_ON_BROKEN_BUILDS
              value: "true"
            - name: GITLAB_NOTIFY_PUSHER
              value: "false"
            - name: GITLAB_BACKUP_SCHEDULE
              value: daily
            - name: GITLAB_BACKUP_TIME
              value: 01:00
            - name: DB_TYPE
              value: postgres
            - name: DB_HOST
              value: postgresql
            - name: DB_PORT
              value: "5432"
            - name: DB_USER
              value: gitlab
            - name: DB_PASS
              value: passw0rd
            - name: DB_NAME
              value: gitlab_production
            - name: REDIS_HOST
              value: redis
            - name: REDIS_PORT
              value: "6379"
          ports.
            - name: http
              containerPort: 80
            - name: ssh
              containerPort: 22
          volumeMounts.
            - mountPath: /home/git/data
              name: data
          livenessProbe.
            httpGet.
              path: /
              port: 80
            initialDelaySeconds: 180
            timeoutSeconds: 5
          readinessProbe.
            httpGet.
              path: /
              port: 80
            initialDelaySeconds: 5
            timeoutSeconds: 1
      volumes.
        - name: data
          persistentVolumeClaim.
            claimName: gitlab-pvc
```

where:

- GITLAB_ROOT_PASSWORD is used to configure the password for the root user login
- GITLAB_HOST is the address of gitlab
- GITLAB_PORT is the gitlab http port
- GITLAB_SSH_PORT is the gitlab ssh port

> PS: Since we will use NodePort for direct access, the address filled here is the Kubernetes cluster node address and the port is the port exposed by NodePort, so you can adjust it according to your node IP when experimenting.

Use `kubectl apply -f gitlab-deploy.yaml` to create the Gitlab, and then use `kubectl get po -n devops | grep gitlab` to see how the Pod was created, and only when the status of the Pod changes to running does that mean it was created successfully, as follows:

![图片描述](assets/lab-deploying-and-using-gitlab-in-kubernetes-11-0.png)
