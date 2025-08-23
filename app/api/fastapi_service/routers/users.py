from fastapi import APIRouter, HTTPException, Request
from core.db.neon import engine
from sqlalchemy import text

router = APIRouter()

@router.get("/")
async def get_users():
    conn = engine.connect()
    res = conn.execute(text("SELECT * FROM users"))
    # conn.execute(text("insert into users (first, last) values ('Jane','Doe')"))
    # conn.commit()
    return [{"id": row[0], "first": row[1], "last": row[2]} for row in res]

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
