from fastapi import APIRouter, Query
from typing import Optional
from fastapi.responses import JSONResponse
import requests
import io
import pandas as pd

from core.prefect.polars import run_polars_pipeline

router = APIRouter()

@router.get("/run")
async def etl_run(
    source: str = Query(..., description="Data source type: csv, json, api"),
    url: Optional[str] = Query(None, description="Custom dataset URL"),
):
    """
    Run ETL for multiple sources: CSV, JSON, API.
    Returns Polars ETL results (preview + summary).
    """
    if not url:
        return JSONResponse({"error": "Dataset URL required"}, status_code=400)

    try:
        # For simplicity, fetch content with requests (can be large)
        resp = requests.get(url)
        resp.raise_for_status()
        content = resp.content

        # Determine file type
        file_type = "csv" if source == "csv" else "json"

        # Run ETL via Polars wrapper
        result = run_polars_pipeline(file_bytes=content, file_type=file_type)

        return {"result": result}

    except requests.HTTPError as e:
        return JSONResponse({"error": f"HTTP error: {e}"}, status_code=400)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
