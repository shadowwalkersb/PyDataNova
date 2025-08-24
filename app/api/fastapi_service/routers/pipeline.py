from fastapi import APIRouter
from fastapi.responses import JSONResponse
from core.pipelines.etl import run_pipeline

router = APIRouter()

@router.post("/run")
async def pipeline_run():
    """Trigger the ETL pipeline and return results"""
    results = run_pipeline()
    return JSONResponse(
        content={"message": "Pipeline finished", "results": results},
        status_code=200
    )

