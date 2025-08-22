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

def create_user(db: str, payload: dict):
    if db in POSTGRES_SESSIONS:
        session = POSTGRES_SESSIONS[db]()
        ins = postgres.users.insert().values(**payload)
        session.execute(ins)
        session.commit()
        return payload
    elif db == "mongo":
        mongo_models.users_collection.insert_one(payload)
        return payload
    else:
        raise ValueError("Unknown DB")

def update_user(db: str, user_id: int, payload: dict):
    if db in POSTGRES_SESSIONS:
        session = POSTGRES_SESSIONS[db]()
        upd = postgres.users.update().where(postgres.users.c.id == user_id).values(**payload)
        session.execute(upd)
        session.commit()
        return payload
    elif db == "mongo":
        mongo_models.users_collection.update_one({"id": user_id}, {"$set": payload})
        return payload
    else:
        raise ValueError("Unknown DB")

def delete_user(db: str, user_id: int):
    if db in POSTGRES_SESSIONS:
        session = POSTGRES_SESSIONS[db]()
        session.execute(postgres.users.delete().where(postgres.users.c.id == user_id))
        session.commit()
        return {"deleted_id": user_id}
    elif db == "mongo":
        mongo_models.users_collection.delete_one({"id": user_id})
        return {"deleted_id": user_id}
    else:
        raise ValueError("Unknown DB")
