from fastapi import APIRouter, Query
from typing import Optional
from fastapi.responses import JSONResponse
from core.prefect.polars import pipeline, polars_parallel

router = APIRouter()
# Multi-source parallel endpoint
@router.post("/polars/multi")
async def polars_multi(sources: dict):
    try:
        results = polars_parallel(sources)
        return {"results": results}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

@router.get("/polars")
async def polars(
    source: str = Query(..., description="Data source type, e.g., csv"),
    dataset: Optional[str] = Query(None, description="Predefined dataset name"),
    csv_url: Optional[str] = Query(None, description="Custom CSV URL"),
):
    if source == "csv":
        if dataset == "nyc_taxi_sample":
            # local or bundled file
            file_path = "data/nyc_taxi_sample.csv"
            result = pipeline(file_path=file_path)
        elif dataset == "custom" and csv_url:
            # fetch directly from provided URL
            result = pipeline(file_url=csv_url)
        else:
            return JSONResponse(
                {"error": "Invalid dataset or missing CSV URL"},
                status_code=400,
            )
        return {"result": result}

@router.get("/pyspark")
async def pyspark():
    # placeholder result, will hook Prefect later
    return {"result": [{"col1": 10, "col2": "X"}, {"col1": 20, "col2": "Y"}]}
