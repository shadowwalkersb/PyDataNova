# Tiltfile for PyDataNova v14 full stack

# Load all Kubernetes manifests
k8s_yaml('k8s/deployment.yaml')

# FastAPI service
docker_build('pydata-v14-fastapi', 'app/api/fastapi_service', dockerfile='app/api/fastapi_service/Dockerfile')
k8s_resource('fastapi', port_forwards=8000)

# Flask service
docker_build('pydata-v14-flask', 'app/api/flask_service', dockerfile='app/api/flask_service/Dockerfile')
k8s_resource('flask', port_forwards=8001)

# Frontend service
docker_build('pydata-v14-frontend', 'app/versions/v14', dockerfile='app/versions/v14/Dockerfile')
k8s_resource('frontend', port_forwards=5500)

# Optional: ETL/pipeline service relies on manifest only
