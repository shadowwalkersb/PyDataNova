from core.db import mongo, supabase, neon

def get_users(db_name):
    db_map = {
        "neon": neon.db,
    }
    db = db_map.get(db_name)
    # query logic depending on DB
    return db.fetch_all_users()
from .. import db
from ..db import elephant, mongo
from ..models import postgres, mongo as mongo_models

# Mapping for Postgres DB sessions
POSTGRES_SESSIONS = {
    "elephant": elephant.sessions["elephant"],
    "supra": db.sessions["supra"],
}

def get_all_users(db: str):
    if db in POSTGRES_SESSIONS:
        session = POSTGRES_SESSIONS[db]()
        query = postgres.users.select()
        return [dict(row) for row in session.execute(query).fetchall()]
    elif db == "mongo":
        return list(mongo_models.users_collection.find({}, {"_id": 0}))
    else:
        raise ValueError("Unknown DB")

def get_user_by_id(db: str, user_id: int):
    if db in POSTGRES_SESSIONS:
        session = POSTGRES_SESSIONS[db]()
        query = postgres.users.select().where(postgres.users.c.id == user_id)
        result = session.execute(query).first()
        return dict(result) if result else None
    elif db == "mongo":
        return mongo_models.users_collection.find_one({"id": user_id}, {"_id": 0})
    else:
        raise ValueError("Unknown DB")
