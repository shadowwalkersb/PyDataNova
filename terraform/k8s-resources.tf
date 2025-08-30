# ---------------- NAMESPACES ----------------
resource "kubernetes_namespace" "monitoring" {
  metadata { name = "monitoring" }
}

resource "kubernetes_namespace" "default_ns" {
  metadata { name = "default" }
}

# ---------------- FASTAPI ----------------
resource "kubernetes_deployment" "fastapi" {
  metadata { name = "fastapi"; namespace = "default" }
  spec {
    replicas = 1
    selector { match_labels = { app = "fastapi" } }
    template {
      metadata { labels = { app = "fastapi" } }
      spec {
        container {
          name  = "fastapi"
          image = "${var.docker_registry}/fastapi:latest"
          port { container_port = 8000 }
        }
      }
    }
  }
}

resource "kubernetes_service" "fastapi" {
  metadata { name = "fastapi"; namespace = "default" }
  spec {
    selector = { app = "fastapi" }
    port {
      port        = 8000
      target_port = 8000
    }
    type = "NodePort"
  }
}

# ---------------- FLASK ----------------
resource "kubernetes_deployment" "flask" {
  metadata { name = "flask"; namespace = "default" }
  spec {
    replicas = 1
    selector { match_labels = { app = "flask" } }
    template {
      metadata { labels = { app = "flask" } }
      spec {
        container {
          name  = "flask"
          image = "${var.docker_registry}/flask:latest"
          port { container_port = 5000 }
        }
      }
    }
  }
}

resource "kubernetes_service" "flask" {
  metadata { name = "flask"; namespace = "default" }
  spec {
    selector = { app = "flask" }
    port { port = 5000; target_port = 5000 }
    type = "NodePort"
  }
}

# ---------------- FRONTEND ----------------
resource "kubernetes_deployment" "frontend" {
  metadata { name = "frontend"; namespace = "default" }
  spec {
    replicas = 1
    selector { match_labels = { app = "frontend" } }
    template {
      metadata { labels = { app = "frontend" } }
      spec {
        container {
          name  = "frontend"
          image = "${var.docker_registry}/frontend:latest"
          port { container_port = 80 }
        }
      }
    }
  }
}

resource "kubernetes_service" "frontend" {
  metadata { name = "frontend"; namespace = "default" }
  spec {
    selector = { app = "frontend" }
    port { port = 80; target_port = 80 }
    type = "NodePort"
  }
}

# ---------------- PROMETHEUS CONFIGMAP ----------------
resource "kubernetes_config_map" "prometheus_config" {
  metadata { name = "prometheus-config"; namespace = kubernetes_namespace.monitoring.metadata[0].name }
  data = {
    "prometheus.yml" = <<-EOT
      global:
        scrape_interval: 15s
      scrape_configs:
        - job_name: 'fastapi'
          metrics_path: /metrics
          static_configs:
            - targets: ['fastapi:8000']
        - job_name: 'flask'
          metrics_path: /metrics
          static_configs:
            - targets: ['flask:5000']
        - job_name: 'frontend'
          metrics_path: /metrics
          static_configs:
            - targets: ['frontend:80']
    EOT
  }
}

# ---------------- PROMETHEUS DEPLOYMENT & SERVICE ----------------
resource "kubernetes_deployment" "prometheus" {
  metadata { name = "prometheus"; namespace = kubernetes_namespace.monitoring.metadata[0].name }
  spec {
    replicas = 1
    selector { match_labels = { app = "prometheus" } }
    template {
      metadata { labels = { app = "prometheus" } }
      spec {
        container {
          name  = "prometheus"
          image = "prom/prometheus:latest"
          args  = ["--config.file=/etc/prometheus/prometheus.yml"]
          port { container_port = 9090 }
          volume_mount {
            name      = "config-volume"
            mount_path = "/etc/prometheus"
          }
        }
        volume {
          name = "config-volume"
          config_map { name = kubernetes_config_map.prometheus_config.metadata[0].name }
        }
      }
    }
  }
}

resource "kubernetes_service" "prometheus" {
  metadata { name = "prometheus"; namespace = kubernetes_namespace.monitoring.metadata[0].name }
  spec {
    selector = { app = "prometheus" }
    port { port = 9090; target_port = 9090 }
    type = "NodePort"
  }
}

# ---------------- GRAFANA ----------------
resource "kubernetes_deployment" "grafana" {
  metadata { name = "grafana"; namespace = kubernetes_namespace.monitoring.metadata[0].name }
  spec {
    replicas = 1
    selector { match_labels = { app = "grafana" } }
    template {
      metadata { labels = { app = "grafana" } }
      spec {
        container {
          name  = "grafana"
          image = "grafana/grafana:latest"
          env {
            name  = "GF_SECURITY_ADMIN_PASSWORD"
            value = "admin"
          }
          port { container_port = 3000 }
        }
      }
    }
  }
}

resource "kubernetes_service" "grafana" {
  metadata { name = "grafana"; namespace = kubernetes_namespace.monitoring.metadata[0].name }
  spec {
    selector = { app = "grafana" }
    port { port = 3000; target_port = 3000 }
    type = "NodePort"
  }
}
