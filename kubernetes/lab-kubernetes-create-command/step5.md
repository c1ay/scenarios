# Create a Configmap

The final step is to create a configMap. A configMap is an object that contains configuration data that can be consumed by pods. To create a configMap, create a file called `configmap.yaml` with the following contents:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: myconfigmap
  namespace: mynamespace
data:
  config: |
    database.host=example.com
    database.port=5432
    database.user=myuser
    database.password=mypassword
```

In this example, we are creating a configMap called `myconfigmap` in the `mynamespace` namespace. The configMap contains a configuration file that can be consumed by pods.

To create the configMap, run the following command:

```bash
kubectl create -f configmap.yaml
```

You can verify that the configMap was created by running the following command:

```bash
kubectl get configmaps -n mynamespace
```

This will display a list of configMaps, including the `myconfigmap` configMap.
