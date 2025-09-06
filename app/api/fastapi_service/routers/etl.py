from fastapi import APIRouter, Query
from typing import Optional
from fastapi.responses import JSONResponse

from core.prefect.polars import run_polars_pipeline

router = APIRouter()


@router.get("/polars")
async def etl_polars(
    source: str = Query(..., description="Data source type, e.g., csv"),
    csv_url: Optional[str] = Query(None, description="Remote CSV URL"),
):
    """
    Run the Polars ETL pipeline.
    Currently supports: CSV source via URL.
    """
    if source == "csv":
        if not csv_url:
            return JSONResponse(
                {"error": "Please provide a CSV URL for the source"},
                status_code=400,
            )
        result = run_polars_pipeline(file_url=csv_url)
        return {"result": result}

    return JSONResponse(
        {"error": f"Source '{source}' not implemented"},
        status_code=400,
    )
