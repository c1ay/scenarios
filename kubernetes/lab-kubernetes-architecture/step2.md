# Kubernetes Node Components

The Kubernetes node components are responsible for running containers and providing the runtime environment for the applications. The node components include:

- **kubelet**: The Kubernetes node agent that runs on each node and is responsible for managing the state of the node and running containers.
- **kube-proxy**: The Kubernetes network proxy that runs on each node and is responsible for routing traffic to the appropriate container.

To check the status of the node components, use the following command:

```bash
kubectl get nodes
```

This command displays the nodes running in the Kubernetes cluster, including the node name, status, and other node information.
