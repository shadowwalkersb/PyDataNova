
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.users import router as users_router

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]
app = FastAPI(title="PyDataNova FastAPI v6")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Welcome to PyDataNova FastAPI v6"}
