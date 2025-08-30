from locust import HttpUser, task, between

class FastAPIUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def analytics_summary(self):
        self.client.get("/analytics/summary")

    @task
    def ml_predict(self):
        self.client.get("/ml/predict?inputText=cat")

class PipelineUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://localhost:8002"  # adjust if pipeline port differs

    @task
    def run_etl(self):
        self.client.get("/v14/run")
