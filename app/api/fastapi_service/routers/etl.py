from fastapi import APIRouter, Query
from typing import Optional
from fastapi.responses import JSONResponse
from core.prefect.polars import pipeline

router = APIRouter()

@router.get("/polars")
async def polars(url=None):
        url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv";
        result = pipeline(url)
        return {"result": result}

@router.get("/pyspark")
async def pyspark():
    # placeholder result, will hook Prefect later
    return {"result": [{"col1": 10, "col2": "X"}, {"col1": 20, "col2": "Y"}]}
