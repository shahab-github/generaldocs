Here's a more streamlined version of your documentation that focuses on using ArgoCD and OIDC configuration for Azure AD authentication:

---

# **Headlamp Dashboard Installation Guide with ArgoCD and OIDC**

This guide outlines how to deploy the **Headlamp** Kubernetes dashboard using a Helm chart managed by ArgoCD, with OIDC authentication configured to work with Azure Active Directory (Azure AD).

---

## **Prerequisites**

1. **Kubernetes Cluster**: A running Kubernetes cluster with ArgoCD installed and configured.
2. **Helm**: Ensure Helm is installed.
3. **Azure Active Directory (AAD)**: You need an Azure AD tenant and app registration for OIDC authentication.
4. **ArgoCD**: Installed and connected to your cluster. See [ArgoCD documentation](https://argo-cd.readthedocs.io/en/stable/getting_started/) for setup instructions.

---

## **Step-by-Step Installation**

### **1. Helm Chart Repository Configuration in ArgoCD**

If not already done, configure your Helm chart repository in ArgoCD by adding it as a Helm repository source.

1. Log in to ArgoCD.
2. Go to **Settings** → **Repositories** → **Connect Repo Using HTTPS**.
3. Add your Helm repository.

### **2. Create the Application in ArgoCD**

You can create a new ArgoCD Application pointing to your Helm chart:

1. Go to **Applications** in ArgoCD.
2. Click **New App** and fill in the following details:

    - **Application Name**: `headlamp`
    - **Project**: Default
    - **Sync Policy**: Automatic (if desired)
    - **Source**:
        - **Repository URL**: `<your-helm-repo-url>`
        - **Chart**: `headlamp`
        - **Target Revision**: `<chart-version>`
        - **Path**: Leave this blank unless you have a specific directory
    - **Destination**:
        - **Cluster**: Your Kubernetes cluster
        - **Namespace**: `kube-system` (or your preferred namespace)

3. Click **Create**.

ArgoCD will sync the Helm chart and deploy Headlamp to your cluster.

### **3. Configure OIDC Authentication with Azure AD**

To configure OIDC for authentication, update your Helm chart’s `values.yaml` file to include Azure AD settings:

```yaml
oidc:
  issuerUrl: "https://login.microsoftonline.com/<your-tenant-id>/v2.0"
  clientId: "<your-client-id>"
  clientSecret: "<your-client-secret>"
  redirectUrl: "https://<your-headlamp-domain>/oidc/callback"
  scopes: ["openid", "profile", "email"]
```

- **issuerUrl**: Replace `<your-tenant-id>` with your Azure AD tenant ID.
- **clientId**: Replace with your registered Azure AD application’s client ID.
- **clientSecret**: Set this to the client secret from your Azure AD app registration.
- **redirectUrl**: Set this to the callback URL for OIDC in your domain.

Ensure that the redirect URL is registered in Azure AD as part of your app’s authentication settings.

### **4. Sync Application in ArgoCD**

Once your `values.yaml` is configured and pushed to the repository, sync the ArgoCD application to deploy or update the Headlamp installation.

---

## **Accessing the Dashboard**

Once the deployment is complete, you can access the Headlamp dashboard through the configured Ingress or service.

- **URL**: Use the URL you set in your `values.yaml` for OIDC (e.g., `https://<your-headlamp-domain>`).
- **Login**: You will be redirected to Azure AD for authentication.

---

## **Uninstalling Headlamp**

To remove the Headlamp dashboard, simply delete the ArgoCD application:

```bash
argocd app delete headlamp
```

---

## **Troubleshooting**

### **OIDC Issues**

1. **Azure AD Redirect Problems**: Ensure the redirect URL is correctly registered in Azure AD.
2. **Token Issues**: If you’re having token issues, verify that the correct scopes (`openid`, `profile`, `email`) are configured in Azure AD and the `values.yaml`.

---

This document provides the steps for deploying the Headlamp dashboard using ArgoCD with OIDC authentication via Azure AD. Adjust the `values.yaml` as needed for your environment.

--- 

This documentation is more focused on your specific setup using ArgoCD and OIDC authentication with Azure AD. Let me know if you need further customization!
