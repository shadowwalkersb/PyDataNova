from fastapi import APIRouter
from fastapi.responses import JSONResponse
from core.pipelines.etl import run_pipeline
from threading import Thread
from uuid import uuid4
from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
import time

app = FastAPI(title="Pipeline Service")

# Simple in-memory store for demo
FLOW_RUNS = {}

@router.post("/run")
async def pipeline_run():
    run_id = str(uuid4())

    def run_bg():
        results = run_pipeline()
        FLOW_RUNS[run_id] = results

    Thread(target=run_bg).start()
    return JSONResponse(content={"run_id": run_id, "message": "Pipeline started"}, status_code=202)

@router.get("/status/{run_id}")
async def pipeline_status(run_id: str):
    results = FLOW_RUNS.get(run_id)
    if results:
        status = {k: "Finished" for k in results.keys()}
    else:
        status = {"csv": "Running", "api": "Running"}
        results = {k: None for k in status.keys()}
    return JSONResponse(content={"tasks": status, "results": results})


# Counter for number of pipeline runs
pipeline_runs = Counter("pipeline_runs_total", "Number of pipeline runs")

@app.post("/v14/run")
def run_pipeline():
    pipeline_runs.inc()
    # your ETL logic here
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


REQUEST_COUNT = Counter("pipeline_requests_total", "Total pipeline requests")
REQUEST_LATENCY = Histogram("pipeline_request_latency_seconds", "Pipeline request latency")

@app.get("/run")
def run_pipeline():
    start = time.time()
    REQUEST_COUNT.inc()
    # mock pipeline work
    time.sleep(1.5)
    REQUEST_LATENCY.observe(time.time() - start)
    return {"status": "pipeline run complete"}
