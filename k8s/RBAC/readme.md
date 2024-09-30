### K8s RBAC 
```sh
# create a namespace
kubectl create ns lockdown

# create service account
kubectl create serviceaccount --namespace lockdown sa-lockdown
```

Creating a read only role for a specific namespace
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: lockdown  # Replace with the actual namespace
  name: view-only-role
rules:
- apiGroups: [""]  # Core API group (for pods, services, configmaps, etc.)
  resources: ["pods", "services", "configmaps", "secrets", "endpoints", "persistentvolumeclaims", "events"]
  verbs: ["get", "list", "watch"]  # View-only permissions
- apiGroups: ["apps"]  # Apps API group (for deployments, replicasets, etc.)
  resources: ["deployments", "replicasets", "statefulsets", "daemonsets"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["batch"]  # Batch API group (for jobs, cronjobs)
  resources: ["jobs", "cronjobs"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["networking.k8s.io"]  # For network-related resources
  resources: ["networkpolicies", "ingresses"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["rbac.authorization.k8s.io"]  # For RBAC-related resources
  resources: ["roles", "rolebindings"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["storage.k8s.io"]  # For storage-related resources
  resources: ["storageclasses"]
  verbs: ["get", "list", "watch"]
```

Now binding the service account to a role to delegate the permission to service account
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: rb-lockdown
subjects:
- kind: ServiceAccount
  name: sa-lockdown
roleRef:
  kind: Role
  name: lockdown
  apiGroup: rbac.authorization.k8s.io
```

You can use the kubectl auth can-i command to check the permissions
```sh
kubectl auth can-i get pods \
        --namespace lockdown \
        --as system:serviceaccount:lockdown:sa-lockdown
```

Reference: https://vpetersson.com/2018/06/15/kubernetes-rbac.html
