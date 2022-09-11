resource "kubernetes_service" "systeminfo" {
  metadata {
    name = "systeminfo"
    labels = {
      app = "systeminfo"
    }
  }
  spec {
    selector = {
      app = kubernetes_deployment.systeminfo.spec.0.template.0.metadata[0].labels.app
    }
    port {
      port        = var.port
      target_port = var.port
    }

    type = "LoadBalancer"
  }
}