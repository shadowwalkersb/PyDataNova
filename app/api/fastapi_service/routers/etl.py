from fastapi import APIRouter
from fastapi.responses import JSONResponse
from core.pipelines.etl import etl_flow

router = APIRouter()
# Multi-source parallel endpoint
@router.post("/polars/multi")
async def etl_polars_multi(sources: dict):
    """
    Run multiple Polars ETL tasks in parallel.
    """
    try:
        results = polars_parallel(sources)
        return {"results": results}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

@router.post("/run")
async def run_pipeline():
    result = etl_flow()
    return JSONResponse(content={"message": f"Pipeline finished. Rows inserted: {result['rows_inserted']}"})

@router.post("/run")
async def pipeline_run():
    """Trigger the ETL pipeline and return results"""
    results = run_pipeline()
    return JSONResponse(
        content={"message": "Pipeline finished", "results": results},
        status_code=200
    )

@router.get("/polars")
async def run_polars_pipeline():
    # placeholder result, will hook Prefect later
    return {"result": [{"col1": 1, "col2": "A"}, {"col1": 2, "col2": "B"}]}

@router.get("/pyspark")
async def etl_pyspark_placeholder():
    return {"message": "PySpark ETL placeholder – not active in v7"}
