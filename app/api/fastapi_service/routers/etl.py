from fastapi import APIRouter, Query
from typing import Optional
from fastapi.responses import JSONResponse

from core.prefect.polars import run_polars_pipeline

router = APIRouter()


@router.get("/polars")
async def etl_polars(
    source: str = Query(..., description="Data source type, e.g., csv"),
    dataset: Optional[str] = Query(None, description="Predefined dataset name"),
    csv_url: Optional[str] = Query(None, description="Custom CSV URL"),
):
    """
    Run the Polars ETL pipeline.
    Currently supports: CSV source.
    """
    if source == "csv":
        if dataset == "nyc_taxi_sample":
            # local or bundled file
            file_path = "data/nyc_taxi_sample.csv"
            result = run_polars_pipeline(file_path=file_path)
        elif dataset == "custom" and csv_url:
            # fetch directly from provided URL
            result = run_polars_pipeline(file_url=csv_url)
        else:
            return JSONResponse(
                {"error": "Invalid dataset or missing CSV URL"},
                status_code=400,
            )
        return {"result": result}

    return JSONResponse(
        {"error": f"Source '{source}' not implemented"},
        status_code=400,
    )
