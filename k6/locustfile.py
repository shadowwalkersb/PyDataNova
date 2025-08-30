from locust import HttpUser, task, between

class FastAPIUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def analytics_summary(self):
        self.client.get("/analytics/summary")

    @task
    def ml_predict(self):
        self.client.get("/ml/predict?inputText=cat")

    @task
    def rpc_echo(self):
        self.client.post("/rpc/echo", json={"message": "test"})

class FlaskUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://localhost:5000"  # adjust if needed

    @task
    def analytics_summary(self):
        self.client.get("/analytics/summary")

    @task
    def ml_predict(self):
        self.client.get("/ml/predict?inputText=dog")

    @task
    def rpc_echo(self):
        self.client.post("/rpc/echo", json={"message": "hello"})

class PipelineUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://localhost:8002"  # adjust to your pipeline service

    @task
    def run_etl(self):
        self.client.get("/v14/run")

class FrontendUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://localhost:80"  # frontend Nginx port

    @task
    def load_main_page(self):
        self.client.get("/")
