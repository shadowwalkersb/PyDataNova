# tests/db/test_connections.py
import os
from sqlalchemy import create_engine, text
from pymongo import MongoClient
from supabase import create_client
from dotenv import load_dotenv

# Load .env at root
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../../.env"))

NEON_URL = os.getenv("NEON_URL")
MONGO_URL = os.getenv("MONGO_URL")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# print("Testing database connections...")
# print(f"NEON_URL: {NEON_URL}")
# print(f"MONGO_URL: {MONGO_URL}")
# print(f"SUPABASE_URL: {SUPABASE_URL}")
# print(f"SUPABASE_KEY: {SUPABASE_KEY}")

# --------------------
# Neon/Postgres Test
# --------------------
def test_neon_connection():
    engine = create_engine(NEON_URL, echo=False)
    with engine.connect() as conn:
        # print(engine.table_names)
        print(conn.tables)
        # result = conn.execute(text("SELECT 1"))
        # assert result.scalar() == 1

# # --------------------
# # MongoDB Test
# # --------------------
# def test_mongo_connection():
#     client = MongoClient(MONGO_URL)
#     db = client.get_database("pydatanova")
#     # Just ensure we can list collections
#     collections = db.list_collection_names()
#     assert isinstance(collections, list)

# # --------------------
# # Supabase Test
# # --------------------
# def test_supabase_connection():
#     client = create_client(SUPABASE_URL, SUPABASE_KEY)
#     response = client.table("users").select("id").limit(1).execute()
#     # Just check response object exists
#     assert response is not None
