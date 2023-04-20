### Create the Jenkins role and authorize it

Create a `jenkins-sa.yaml` file in the `/home/shiyanlou/Code/devops/sy-02-1` directory and write the following:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata.
  name: jenkins-sa
  namespace: devops

---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata.
  name: jenkins-cr
rules.
  - apiGroups: ["extensions", "apps"]
    resources: ["deployments"]
    verbs: ["create", "delete", "get", "list", "watch", "patch", "update"]
  - apiGroups: [""]
    resources: ["services"]
    verbs: ["create", "delete", "get", "list", "watch", "patch", "update"]
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["create", "delete", "get", "list", "patch", "update", "watch"]
  - apiGroups: [""]
    resources: ["pods/exec"]
    verbs: ["create", "delete", "get", "list", "patch", "update", "watch"]
  - apiGroups: [""]
    resources: ["pods/log"]
    verbs: ["get", "list", "watch"]
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata.
  name: jenkins-crd
roleRef.
  kind: ClusterRole
  name: jenkins-crd
  apiGroup: rbac.authorization.k8s.io
subjects.
  - kind: ServiceAccount
    name: jenkins-sa
    namespace: devops
```

Then use `kubectl apply -f jenkins-sa.yaml` to create the Jenkins role and complete the authorization, with the following output:

![图片描述](https://doc.shiyanlou.com/courses/10022/2123746/0f0d3b72a73972b5d7388410f9272ec8-0/wm)
