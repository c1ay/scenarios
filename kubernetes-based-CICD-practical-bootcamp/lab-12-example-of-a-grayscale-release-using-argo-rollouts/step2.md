## Argo rollouts

Argo rollouts is a Kubernetes Controller and corresponding series of CRDs that provide more powerful Deployment capabilities. It includes features such as grayscale releases, blue-green deployments, update testing (experimentation), and progressive delivery.

Supported features are as follows:
● Blue-green update policy
● Canary update policy
● Fine-grained, weighted traffic shifting
● Automatic rollback and promotion
● Manual judgment
● Customizable metrics query and business KPI analysis
● Entry Controller Integration: NGINX, ALB
● Service grid integration: Istio, Linkerd, SMI
● Metric provider integration: Prometheus, Wavefront, Kayenta, Web, Kubernetes Jobs

Argo rollouts are similar to Deployment, but with enhanced rollout policies and traffic control. When spec.template sends a change, Argo rollouts will rollout according to spec.strategy, usually creating a new ReplicaSet and gradually scaling down the number of pods in the previous ReplicaSet.
