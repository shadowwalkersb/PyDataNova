from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/run")
async def run_pipeline():
    return JSONResponse(content={"message": "Pipeline started"}, status_code=202)
