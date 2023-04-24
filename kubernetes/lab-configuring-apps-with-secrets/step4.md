# Mount The Secret As A Volume In A Pod

Now that we have created the secret, we can mount it as a volume in a pod. We will create a simple pod that reads the secret value from the mounted volume and outputs it to the console.

Create a file named `pod.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-pod
spec:
  containers:
    - name: secret-container
      image: nginx
      volumeMounts:
        - name: secret-volume
          mountPath: /etc/secret-volume
  volumes:
    - name: secret-volume
      secret:
        secretName: my-secret
```

Apply the pod configuration:

```bash
kubectl apply -f pod.yaml
```
