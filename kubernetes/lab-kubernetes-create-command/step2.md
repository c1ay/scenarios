# Create a Deployment

The next step is to create a deployment. A deployment manages a set of replicas of a pod template. To create a deployment, create a file called `deployment.yaml` with the following contents:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mydeployment
  namespace: mynamespace
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: mycontainer
          image: nginx
```

Then, run the following command to create the deployment:

```bash
kubectl create -f deployment.yaml
```

This will create a deployment called `mydeployment` in the `mynamespace` namespace. The deployment will manage 3 replicas of a pod template that runs an Nginx container.

You can verify that the deployment was created by running the following command:

```bash
kubectl get deployments -n mynamespace
```

This will display a list of deployments, including the `mydeployment` deployment.
