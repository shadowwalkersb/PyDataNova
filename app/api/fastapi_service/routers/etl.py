from fastapi import APIRouter
from fastapi.responses import JSONResponse
from core.prefect.polars_parallel import polars_parallel


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

# PySpark placeholder endpoint
@router.get("/pyspark")
async def etl_pyspark_placeholder():
    return {"message": "PySpark ETL placeholder – not active in v7"}
