# Create a Secret

The next step is to create a secret. A secret is an object that contains sensitive data, such as passwords or API keys. To create a secret, create a file called `secret.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
  namespace: mynamespace
type: Opaque
data:
  username: dXNlcm5hbWU=
  password: cGFzc3dvcmQ=
```

In this example, we are creating a secret called `mysecret` in the `mynamespace` namespace. The secret contains a username and password encoded in Base64 format.

To create the secret, run the following command:

```bash
kubectl create -f secret.yaml
```

You can verify that the secret was created by running the following command:

```bash
kubectl get secrets -n mynamespace
```

This will display a list of secrets, including the `mysecret` secret.
