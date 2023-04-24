# Kubernetes Pod Components

The Kubernetes pod is the smallest deployable unit in Kubernetes, representing a single instance of a running process in the cluster. Each pod consists of one or more containers that share the same network namespace and storage volumes. The pod components include:

- **pause container**: The pause container is a special container that runs in every pod and is responsible for holding the network namespace open and sharing it with other containers in the pod.
- **application container(s)**: The application container(s) run in the pod and execute the application code.

Create a file called `simple-pod.yaml` with the following content:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: simple-pod
spec:
  containers:
    - name: simple-container
      image: nginx
```

This YAML file creates a pod with a single container that runs the nginx image.

To create the pod, run the following command:

```bash
kubectl apply -f simple-pod.yaml
```

To check the status of the pod, use the following command:

```bash
kubectl get pods
```

This command displays the pods running in the Kubernetes cluster, including the pod name, namespace, status, and other pod information.
