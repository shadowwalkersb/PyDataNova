from fastapi import FastAPI
from api.fastapi.routers import users, items

app = FastAPI(title="PyDataNova FastAPI v6")

# Include routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])
