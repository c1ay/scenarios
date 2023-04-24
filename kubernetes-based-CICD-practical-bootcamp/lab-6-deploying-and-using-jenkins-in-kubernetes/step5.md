### Deploy the Jenkins application

Create a `jenkins-deploy.yaml` file in the `/home/shiyanlou/Code/devops/sy-02-1` directory, and write the following:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata.
  name: jenkins
  namespace: devops
spec.
  selector.
    matchLabels.
      app: jenkins
  replicas: 1
  template.
    metadata.
      labels.
        app: jenkins
    spec.
      terminationGracePeriodSeconds: 10
      serviceAccount: jenkins-sa
      containers.
        - name: jenkins
          image: jenkins/jenkins:lts
          imagePullPolicy: IfNotPresent
          env.
            - name: JAVA_OPTS
              value: -XshowSettings:vm -Dhudson.slaves.NodeProvisioner.initialDelay=0 -Dhudson.slaves.NodeProvisioner.MARGIN=50 -Dhudson.slaves. NodeProvisioner.MARGIN0=0.85 -Duser.timezone=Asia/Shanghai
          ports.
            - containerPort: 8080
              name: web
              protocol: TCP
            - containerPort: 50000
              name: agent
              protocol: TCP
          resources.
            limits.
              cpu: 1000m
              memory: 1Gi
            requests.
              cpu: 500m
              memory: 512Mi
          livenessProbe.
            httpGet.
              path: /login
              port: 8080
            initialDelaySeconds: 60
            timeoutSeconds: 5
            failureThreshold: 12
          readinessProbe.
            httpGet.
              path: /login
              port: 8080
            initialDelaySeconds: 60
            timeoutSeconds: 5
            failureThreshold: 12
          volumeMounts.
            - name: jenkinshome
              mountPath: /var/jenkins_home
      securityContext.
        fsGroup: 1000
      volumes.
        - name: jenkinshome
          persistentVolumeClaim.
            claimName: jenkins-pvc
```

Then use `kubectl apply -f jenkins-deploy.yaml` to deploy Jenkins, then use `kubectl get pod -n devops | grep jenkins` to check the application deployment status, only when the application becomes `Running` it means the deployment is successful, as follows:

![图片描述](assets/lab-deploying-and-using-jenkins-in-kubernetes-4-0.png)
