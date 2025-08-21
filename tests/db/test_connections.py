from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text
from pymongo import MongoClient
from supabase import create_client

# Load .env at root
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../../.env"))


# Load env variables
NEON_URL = os.getenv("NEON_URL")
MONGO_URL = os.getenv("MONGO_URL")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# --------------------
# Neon/Postgres Test
# --------------------
def test_neon():
    try:
        engine = create_engine(NEON_URL, echo=True)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("Neon connected:", result.scalar())
    except Exception as e:
        print("Neon connection failed:", e)

# --------------------
# MongoDB Test
# --------------------
def test_mongo():
    try:
        client = MongoClient(MONGO_URL)
        db = client.get_database("pydatanova")
        print("MongoDB connected:", db.list_collection_names())
    except Exception as e:
        print("MongoDB connection failed:", e)

# --------------------
# Supabase Test
# --------------------
def test_supabase():
    try:
        client = create_client(SUPABASE_URL, SUPABASE_KEY)
        data = client.table("users").select("id").limit(1).execute()
        print("Supabase connected:", data.data)
    except Exception as e:
        print("Supabase connection failed:", e)

# --------------------
# Run all tests
# --------------------
if __name__ == "__main__":
    print("Testing all DB connections...\n")
    test_neon()
    test_mongo()
    test_supabase()
