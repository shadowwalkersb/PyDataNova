from fastapi import APIRouter
from core.prefect.polars import etl as polars_etl

router = APIRouter()

@router.get("/polars")
async def polars():
    return {"result": polars_etl()}

@router.get("/pyspark")
async def pyspark():
    # placeholder result, will hook Prefect later
    return {"result": [{"col1": 10, "col2": "X"}, {"col1": 20, "col2": "Y"}]}
