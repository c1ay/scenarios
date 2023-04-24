# Create a Pod

Create a simple pod that will be used as the template for the replicas. Create a file called `/home/labex/project/myapp-pod.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
spec:
  containers:
    - name: myapp-container
      image: nginx
      ports:
        - containerPort: 80
```

Create the pod using the following command:

```shell
kubectl apply -f /home/labex/project/myapp-pod.yaml
```
