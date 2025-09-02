from fastapi import APIRouter, HTTPException
from core.db.neon import fastapi_engine
import pandas as pd
from sqlalchemy import text

router = APIRouter()

@router.get("/")
async def get_users():
    query = "SELECT * FROM users;"
    try:
        async with fastapi_engine.connect() as conn:
            # Pandas only supports sync reads, use run_sync
            df = await conn.run_sync(lambda sync_conn: pd.read_sql(text(query), sync_conn))
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
