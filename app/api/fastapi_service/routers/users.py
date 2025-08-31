from fastapi import APIRouter, HTTPException
from core.db.neon import fastapi_engine
import pandas as pd
from sqlalchemy import text
from pydantic import BaseModel

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

# Pydantic model for request body
class User(BaseModel):
    first: str
    last: str

@router.post("/")
async def add_user(user: User):
    query = """
    INSERT INTO users (first, last)
    VALUES (:first, :last)
    RETURNING id, first, last;
    """
    async with fastapi_engine.begin() as conn:
        try:
            result = await conn.execute(text(query), {"first": user.first, "last": user.last})
            new_user = result.fetchone()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    return dict(new_user._mapping)

@router.post("/")
async def add_user(request: Request):
    data = await request.json()  # raw JSON
    print(data)
    first = data.get("first")
    last = data.get("last")
    if not first or not last:
        raise HTTPException(status_code=400, detail="Missing first or last name")

    with engine.begin() as conn:  # auto-commit
        conn.execute(
            text("INSERT INTO users (first, last) VALUES (:first, :last)"),
            {"first": first, "last": last}
        )
    return {"status": "ok"}
    # return [
    #     { "id": 1, "name": "John Doe", "email": "john@example.com" },
    #     { "id": 2, "name": "Jane Smith", "email": "jane@example.com" },
    #     { "id": 3, "name": "Alice Johnson", "email": "alice@example.com" }
    #     ]
