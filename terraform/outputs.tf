output "fastapi_url" { value = kubernetes_service.fastapi.status[0].load_balancer[0].ingress[0].ip }
output "flask_url"   { value = kubernetes_service.flask.status[0].load_balancer[0].ingress[0].ip }
output "frontend_url" { value = kubernetes_service.frontend.status[0].load_balancer[0].ip }
output "prometheus_url" { value = kubernetes_service.prometheus.status[0].load_balancer[0].ip }
output "grafana_url" { value = kubernetes_service.grafana.status[0].load_balancer[0].ip }
