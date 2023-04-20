### Developing Ingress

The Service described above is mainly used inside the cluster, but NodePort and LoadBalancer types can also be used for external access, but they have some drawbacks:

- If you use the NodePort type, you need to maintain the port address of each application, which is not easy to manage if there are too many services
- If you use the LoadBalancer type, it is basically used on the cloud, which requires more IPs and is more expensive
- Both NodePort and LoadBalancer work at layer 4, and cannot directly perform SSL checksum for HTTPS type requests

Therefore, the community provides the Ingress object to provide a unified entry point to the cluster, with the following logic:
![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/c80ebde4db1520210144d14708fd74b7-0/wm)

The Ingress proxy is not the Service of the Pod, but the Pod. The reason why the Service is configured in the configuration is to get the information of the Pod.

If you want to use Ingress, you must install the Ingress Controller, which we use here as an example: `Nginx ingrss controller`.

#### Installing the Nginx ingress controller

If you use the official default installation method, it is difficult to download the image. For this experiment, we have specifically downloaded the image and uploaded it to our domestic repository, where it can be deployed directly using the following command:

```bash
kubectl apply -f https://raw.githubusercontent.com/joker-bai/kubernetes-software-yaml/main/ingress/nginx/ingress-nginx.yaml
```

ingress-controller will be deployed under the `ingress-nginx` namespace, so we can use `kubectl get pod -n ingress-nginx` to check the deployment status, and a pod with a status of `running` indicates a successful deployment, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/582ec2b941de38e58062bac596400c3d-0/wm)

#### Exposing the ingress-nginx service

Create the `ingress-svc.yaml` file in the `/home/shiyanlou/Code/devops/sy-01-1` directory and write the following:

```yaml
apiVersion: v1
kind: Service
metadata.
  labels.
    app.kubernetes.io/name: ingress-nginx
  name: ingress-nginx-controller-svc
  namespace: ingress-nginx
spec.
  ports.
    - appProtocol: http
      name: http
      nodePort: 30080
      port: 80
      protocol: TCP
      targetPort: http
    - appProtocol: https
      name: https
      nodePort: 30443
      port: 443
      protocol: TCP
      targetPort: https
  selector.
    app.kubernetes.io/component: controller
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/name: ingress-nginx
  type: NodePort
```

Then execute the command `kubectl apply -f ingress-svc.yaml` to deploy it, and use `kubectl get service -n ingress-nginx` to see information about the ingress-controller Service, as follows:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/acbcc8ca42ca658f717910bcb5fbaed4-0/wm)

Since ingress-controller is also a Pod, it needs to be exposed to be accessed, so the above Service can be accessed via NodePort.

#### Configuring Ingress for Nginx Applications

Create the `nginx-ingress.yaml` file in the `/home/shiyanlou/Code/devops/sy-01-1` directory and write the following:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata.
  name: nginx
  annotations.
    kubernetes.io/ingress.class: "nginx"
spec.
  rules.
    - host: nginx.devops.com
      http.
        paths.
          - path: /
            backend.
              service.
                name: nginx
                port.
                  number: 80
            pathType: Prefix
```

Then use `kubectl apply -f nginx-ingress.yaml` to create the Ingress, and after execution, use `kubectl get ingress` to check the creation status, as follows

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/721faeba3f6bcb18422cfd442aff5c82-0/wm)

#### Configure domain name resolution and access

But now we can't access it directly because the domain name is not resolved, so for convenience, it is resolved directly in the local hosts.

Open the hosts file with the command `sudo vim /etc/hosts` and insert the following at the end:

```shell
10.111.127.141 nginx.devops.com
```

> PS: The IP address is any node IP of the Kubernetes cluster, change it accordingly.

Then open your browser and type `http://nginx.devops.com:30080` to access it, and the following indicates that it can be accessed properly:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/4f2ea4b905a76a645737acdbb28cbb48-0/wm)

At this point, we can create Ingress properly and access it through the domain name.
