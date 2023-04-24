# Kubernetes Service Components

The Kubernetes service is an abstraction that defines a logical set of pods and a policy by which to access them. The service components include:

- **Service IP**: A virtual IP address assigned to the service that allows applications to access the pods running behind the service.
- **Service Port**: A port number assigned to the service that allows applications to access the pods running behind the service.
- **Endpoint**: A list of IP addresses and port numbers that point to the pods running behind the service.

Create a file called `nginx-service.yaml` with the following content:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

This YAML file creates a service that selects pods with the label `app: nginx` and exposes port 80.

To create the service, run the following command:

```bash
kubectl apply -f nginx-service.yaml
```

To check the status of the service, use the following command:

```bash
kubectl get services
```

This command displays the services running in the Kubernetes cluster, including the service name, namespace, cluster IP, and other service information.
