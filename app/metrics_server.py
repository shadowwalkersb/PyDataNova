from prometheus_client import Counter, start_http_server

frontend_hits = Counter("frontend_hits_total", "Number of frontend requests")

# Start metrics server on port 8001
start_http_server(8001)

# In your real frontend, increment when users load page or click button
# frontend_hits.inc()
