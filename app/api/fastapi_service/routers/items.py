from fastapi import APIRouter, HTTPException
from core.db.neon import fastapi_engine
import pandas as pd
from sqlalchemy import text
from pydantic import BaseModel

router = APIRouter()

@router.get("/")
async def get_items():
    query = "SELECT * FROM items;"
    try:
        async with fastapi_engine.connect() as conn:
            # Pandas only supports sync reads, so use `run_sync` to bridge
            df = await conn.run_sync(lambda sync_conn: pd.read_sql(text(query), sync_conn))
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Pydantic model for request body
class Item(BaseModel):
    name: str
    category: str
    price: float
    owner_id: int

@router.post("/")
async def add_item(item: Item):
    query = """
    INSERT INTO items (name, category, price, owner_id)
    VALUES (:name, :category, :price, :owner_id)
    RETURNING id, name, category, price, owner_id;
    """
    async with fastapi_engine.begin() as conn:
        try:
            result = await conn.execute(text(query), {"name": item.name, "category": item.category, "price": item.price, "owner_id": item.owner_id})
            new_item = result.fetchone()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    return dict(new_item._mapping)
