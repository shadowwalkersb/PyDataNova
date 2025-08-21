from core.db import mongo, supabase, neon

def get_users(db_name):
    db_map = {
        "neon": neon.db,
    }
    db = db_map.get(db_name)
    # query logic depending on DB
    return db.fetch_all_users()
