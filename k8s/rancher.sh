#!/bin/bash

# 1. Add the Helm repository for cert-manager:
helm repo add jetstack https://charts.jetstack.io

# 2. Update your Helm repositories:
helm repo update

# 3. Install cert-manager:
kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/v1.12.0/cert-manager.crds.yaml
helm install cert-manager jetstack/cert-manager --namespace cert-manager --create-namespace --version v1.12.0

# 4. Verify the installation:
kubectl get pods --namespace cert-manager


# Step 2: Install Rancher
# 1. Add the Rancher Helm chart repository:
helm repo add rancher-latest https://releases.rancher.com/server-charts/latest

# 2. Update your Helm repositories:
helm repo update

# 3. Create a namespace for Rancher:
kubectl create namespace cattle-system

# 4. Install Rancher with Helm:
# For production
helm install rancher rancher-latest/rancher --namespace cattle-system --set hostname=rancher.example.com --set ingress.tls.source=letsEncrypt --set letsEncrypt.email=<your-email>

# For development (self-signed certificate):
# helm install rancher rancher-latest/rancher --namespace cattle-system --set hostname=<rancher.example.com> --set bootstrapPassword=<password>

# 5. Verify the Rancher installation:
kubectl -n cattle-system rollout status deploy/rancher
kubectl get pods -n cattle-system


