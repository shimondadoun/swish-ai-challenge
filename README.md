# swish-ai-challenge
 swish.ai challenge for candidate

## How to use:

### Clone this project:
```
git clone git@github.com:shimondadoun/swish-ai-challenge.git
```

### Build the image:


```
docker build .
```
### Option 1 - Run on Docker:
The container uses environment variable to define the port to listen to. so you need to supply the _port_ which the app listen to , run:

```
docker run --name {container_name} --env PORT={port} -p {port_in_container}:{port_in_host} -d {image}
```

### Option 2 - Run on local Kubernetes (using k3d):

First, you need to create Kubernetes cluster. see [k3d cluster create](https://k3d.io/v5.4.6/usage/commands/k3d_cluster_create/).
Second, [install terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli).

When you have the cluster up and running, use terraform to deploy this app to your cluster.

On project repo:

```
cd terraform
```

Now, edit the terraform.tfvars file and fill those variables: 

image - the image tag to deploy.

k8s_address: your cluster's address.

replicas: the number of replicas that you want to deploy.
config_context: the config context to use. if you don't have one, just run:

 ``` kubectl config set-context {name}  --cluster={cluster's name} ``` 

(If you use several namespaces, add the namespace to this command).

#### Run terraform commands:
``` terraform init ``` to initialize the providers.

``` terraform apply ``` to execute the deploy.