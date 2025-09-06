from fastapi import APIRouter
from fastapi.responses import JSONResponse
from core.prefect.orchestrate import orchestrate_pipelines

router = APIRouter(prefix="/etl", tags=["ETL-Orchestration"])

@router.post("/run")
async def run_orchestration(sources: dict):
    try:
        results = orchestrate_pipelines(sources)
        return {"results": results}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
