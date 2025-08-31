from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_service.routers.users import router as users_router
from fastapi_service.routers.items import router as items_router

app = FastAPI(title="PyDataNova FastAPI")

origins = [
    "https://shadowwalkersb.github.io",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(items_router, prefix="/items", tags=["items"])

@app.get("/")
async def root():
    return {"message": "PyDataNova FastAPI Service running..."}
