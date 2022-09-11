resource "kubernetes_deployment" "systeminfo" {
  metadata {
    name = "systeminfo"
  }
  spec {
    selector {
      match_labels = {
        app = "systeminfo"
      }
    }
    replicas = var.replicas
    template {
      metadata {
        labels = {
          app = "systeminfo"
        }
      }
      spec {
        container {
          name  = "systeminfo"
          image = var.image
          env {
            name  = "PORT"
            value = var.port
          }
          port {
            container_port = var.port
          }
        }
      }
    }
  }
}