terraform {
  required_version = "~> 1.2.8"
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 1.13"
    }
  }
  backend "local" {
    path = "./terraform.tfstate"
  }
}

provider "kubernetes" {
  config_context = var.config_context
  host           = var.k8s_address
}