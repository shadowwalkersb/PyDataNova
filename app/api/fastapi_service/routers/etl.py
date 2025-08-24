from fastapi import APIRouter, Query
from typing import Optional
from fastapi.responses import JSONResponse
from core.prefect.polars import pipeline, polars_parallel
from core.pipelines.etl import etl_flow

router = APIRouter()
# Multi-source parallel endpoint
@router.post("/polars/multi")
async def polars_multi(sources: dict):
    """
    Run multiple Polars ETL tasks in parallel.
    """
    try:
        results = polars_parallel(sources)
        return {"results": results}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

@router.post("/run")
async def polars():
    result = etl_flow()
    return JSONResponse(content={"message": f"Pipeline finished. Rows inserted: {result['rows_inserted']}"})

@router.post("/run")
async def pipeline_run():
    results = run_pipeline()
    return JSONResponse(
        content={"message": "Pipeline finished", "results": results},
        status_code=200
    )

@router.get("/pyspark")
async def pyspark():
    # placeholder result, will hook Prefect later
    return {"result": [{"col1": 10, "col2": "X"}, {"col1": 20, "col2": "Y"}]}
