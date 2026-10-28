from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
import os
from dotenv import load_dotenv

load_dotenv()

NEON_URL = os.getenv("NEON_URL")
if not NEON_URL:
    raise ValueError("❌ NEON_URL not set in .env file")

sync_url = NEON_URL
if sync_url.startswith("postgresql://"):
    # Use the driver installed by psycopg2-binary instead of relying on the
    # default driver choice of whichever SQLAlchemy version is installed.
    sync_url = sync_url.replace("postgresql://", "postgresql+psycopg2://", 1)

flask_engine = create_engine(sync_url, pool_pre_ping=True)

async_url = NEON_URL.split("?")[0]  # strip query params
if async_url.startswith("postgresql://"):
    async_url = async_url.replace("postgresql://", "postgresql+asyncpg://", 1)

fastapi_engine = create_async_engine(
    async_url,
    echo=False,
    pool_pre_ping=True
)
