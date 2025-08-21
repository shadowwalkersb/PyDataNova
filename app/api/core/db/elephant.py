# core/db/elephant.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

ELEPHANT_URL = os.getenv("ELEPHANT_URL", "postgresql://user:pass@host:port/dbname")

engine = create_engine(ELEPHANT_URL)
SessionLocal = sessionmaker(bind=engine)
