from fastapi import APIRouter
from fastapi.responses import JSONResponse
from core.pipelines.etl import etl_flow

router = APIRouter()

@router.post("/run")
async def run_pipeline():
    result = etl_flow()
    return JSONResponse(content={"message": f"Pipeline finished. Rows inserted: {result['rows_inserted']}"})
