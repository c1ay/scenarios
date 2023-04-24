# Create a Service

The next step is to create a service. A service is an abstract way to expose an application running on a set of pods as a network service. To create a service, create a file called `service.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: myservice
  namespace: mynamespace
spec:
  selector:
    app: myapp
  ports:
    - name: http
      port: 80
      targetPort: 80
```

Then, run the following command to create the service:

```bash
kubectl create -f service.yaml
```

This will create a service called `myservice` in the `mynamespace` namespace. The service will select pods with the label `app=myapp` and expose port 80.

You can verify that the service was created by running the following command:

```bash
kubectl get services -n mynamespace
```

This will display a list of services, including the `myservice` service.
