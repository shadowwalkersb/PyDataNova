from .. import db
from ..db import elephant, mongo
from ..models import postgres, mongo as mongo_models

# Mapping for Postgres DB sessions
POSTGRES_SESSIONS = {
    "elephant": elephant.sessions["elephant"],
    "supra": db.sessions["supra"],
}

def get_all_items(db: str):
    if db in POSTGRES_SESSIONS:
        session = POSTGRES_SESSIONS[db]()
        query = postgres.items.select()
        return [dict(row) for row in session.execute(query).fetchall()]
    elif db == "mongo":
        return list(mongo_models.items_collection.find({}, {"_id": 0}))
    else:
        raise ValueError("Unknown DB")

def get_item_by_id(db: str, item_id: int):
    if db in POSTGRES_SESSIONS:
        session = POSTGRES_SESSIONS[db]()
        query = postgres.items.select().where(postgres.items.c.id == item_id)
        result = session.execute(query).first()
        return dict(result) if result else None
    elif db == "mongo":
        return mongo_models.items_collection.find_one({"id": item_id}, {"_id": 0})
    else:
        raise ValueError("Unknown DB")

def create_item(db: str, payload: dict):
    if db in POSTGRES_SESSIONS:
        session = POSTGRES_SESSIONS[db]()
        ins = postgres.items.insert().values(**payload)
        session.execute(ins)
        session.commit()
        return payload
    elif db == "mongo":
        mongo_models.items_collection.insert_one(payload)
        return payload
    else:
        raise ValueError("Unknown DB")

def update_item(db: str, item_id: int, payload: dict):
    if db in POSTGRES_SESSIONS:
        session = POSTGRES_SESSIONS[db]()
        upd = postgres.items.update().where(postgres.items.c.id == item_id).values(**payload)
        session.execute(upd)
        session.commit()
        return payload
    elif db == "mongo":
        mongo_models.items_collection.update_one({"id": item_id}, {"$set": payload})
        return payload
    else:
        raise ValueError("Unknown DB")

def delete_item(db: str, item_id: int):
    if db in POSTGRES_SESSIONS:
        session = POSTGRES_SESSIONS[db]()
        session.execute(postgres.items.delete().where(postgres.items.c.id == item_id))
        session.commit()
        return {"deleted_id": item_id}
    elif db == "mongo":
        mongo_models.items_collection.delete_one({"id": item_id})
        return {"deleted_id": item_id}
    else:
        raise ValueError("Unknown DB")
