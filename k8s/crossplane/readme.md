#### Introduction to Crossplane






Tips & Tricks
#### Remove Finalizers to Force Delete
To force delete the resource, remove the finalizer using a kubectl patch command:
```sh
kubectl patch <resource> <resource-name> --type merge -p '{"metadata":{"finalizers":[]}}'
```
