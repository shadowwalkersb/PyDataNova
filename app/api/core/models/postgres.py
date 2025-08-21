from sqlalchemy import Column, String, Integer, Table, MetaData

metadata = MetaData()

users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String),
    Column("email", String)
)

items = Table(
    "items", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String),
    Column("owner_id", Integer)
)
