git clone https://github.com/kodekloudhub/amazon-elastic-kubernetes-service-course.git
cd amazon-elastic-kubernetes-service-course/eks
terraform init
terraform plan
terraform apply --auto-approve

# adding worker nodes to the cluster
aws eks update-kubeconfig --region us-east-1 --name demo-eks
curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/cloudformation/2020-10-29/aws-auth-cm.yaml

terraform output
# Replace the placeholder text <ARN of instance role (not instance profile)> with the value of NodeInstanceRole from Terraform, then save and exit the editor. The ConfigMap should look like this:
# vi aws-auth-cm.yaml
