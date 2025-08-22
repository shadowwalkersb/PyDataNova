from fastapi import APIRouter
from core.db.neon import engine
from sqlalchemy import text
# import pandas as pd

router = APIRouter()

@router.get("/")
async def get_users():
    conn = engine.connect()
    res = conn.execute(text("SELECT * FROM users"))
    # conn.execute(text("insert into users (first, last) values ('Jane','Doe')"))
    # conn.commit()
    return [{"id": row[0], "first": row[1], "last": row[2]} for row in res]
