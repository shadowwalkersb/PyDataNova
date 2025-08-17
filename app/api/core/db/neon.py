from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
import os
from dotenv import load_dotenv

load_dotenv()

NEON_URL = os.getenv("NEON_URL")
if not NEON_URL:
    raise ValueError("❌ NEON_URL not set in .env file")

flask_engine = create_engine(NEON_URL, pool_pre_ping=True)

async_url = NEON_URL.split("?")[0]  # strip query params
if async_url.startswith("postgresql://"):
    async_url = async_url.replace("postgresql://", "postgresql+asyncpg://", 1)

fastapi_engine = create_async_engine(
    async_url,
    echo=False,
    pool_pre_ping=True
)
