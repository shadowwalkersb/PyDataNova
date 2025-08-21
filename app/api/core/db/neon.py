from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
NEON_URL = os.getenv("NEON_URL")
engine = create_engine(NEON_URL)
