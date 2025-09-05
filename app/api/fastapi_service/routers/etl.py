from fastapi import APIRouter

from fastapi_service.core.prefect.polars import polars
from fastapi_service.core.prefect.pyspark import pyspark

router = APIRouter()

@router.get("/polars")
async def run_polars_pipeline():
    # placeholder result, will hook Prefect later
    return {"result": [{"col1": 1, "col2": "A"}, {"col1": 2, "col2": "B"}]}

@router.get("/pyspark")
async def run_pyspark_pipeline():
    # placeholder result, will hook Prefect later
    return {"result": [{"col1": 10, "col2": "X"}, {"col1": 20, "col2": "Y"}]}

@router.get("/polars")
async def run_polars_pipeline():
    return {"result": polars()}

@router.get("/pyspark")
async def run_pyspark_pipeline():
    return {"result": pyspark()}
