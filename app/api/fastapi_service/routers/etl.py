from fastapi import APIRouter

router = APIRouter()

@router.get("/polars")
async def run_polars_pipeline():
    # placeholder result, will hook Prefect later
    return {"result": [{"col1": 1, "col2": "A"}, {"col1": 2, "col2": "B"}]}

@router.get("/pyspark")
async def run_pyspark_pipeline():
    # placeholder result, will hook Prefect later
    return {"result": [{"col1": 10, "col2": "X"}, {"col1": 20, "col2": "Y"}]}
