### Overview
It is a web-based Kubernetes dashboard that simplifies cluster management by providing a user-friendly graphical interface. 
It allows users to interact with and manage Kubernetes resources such as Pods, Services, and Deployments without needing to use the command line.


### Role-Based Access Control (RBAC) in Headlamp
Kubernetes implements Role-Based Access Control (RBAC) to manage access to resources within the cluster. 
RBAC allows you to define which users or groups can perform certain actions on resources like Pods, Deployments, and Nodes. 
Headlamp integrates seamlessly with Kubernetes’ RBAC system to ensure that users can only view or modify resources based on their roles and permissions.

### How RBAC Works in Kubernetes
RBAC works by assigning roles and role bindings to users or groups. What actions are allowed on certain resources (e.g., Pods, Services).
A role defines a set of permissions (rules) to access resources. 
A role binding associates a role with specific users or groups, allowing them to perform the actions defined by the role.


### RBAC and Headlamp
Headlamp honors the RBAC configuration of your Kubernetes cluster, ensuring that users can only access the resources and namespaces for which they have permissions. 
This enhances security and prevents unauthorized access to critical resources.


Key Components of RBAC:
Roles: Define what actions are allowed on certain resources (e.g., Pods, Services).

ClusterRoles: Apply at the cluster-wide level and can control resources across all namespaces.
Roles: Apply at the namespace level, restricting access to resources within a specific namespace.
RoleBindings: Bind a role to a user or group within a namespace.

ClusterRoleBindings: Bind ClusterRoles to users or groups at the cluster level.
RoleBindings: Bi
