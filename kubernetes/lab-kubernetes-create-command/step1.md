# Create a Namespace

The first step is to create a namespace. A namespace is a way to divide cluster resources between multiple users. To create a namespace, create a file called `namespace.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: mynamespace
```

Then, run the following command to create the namespace:

```bash
kubectl create -f namespace.yaml
```

This will create a namespace called `mynamespace`. You can verify that the namespace was created by running the following command:

```bash
kubectl get namespaces
```

This will display a list of namespaces, including the `mynamespace` namespace.
