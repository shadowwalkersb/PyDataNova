from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_service.routers.users_mock import router as users_mock_router
from fastapi_service.routers.items_mock import router as items_mock_router
from fastapi_service.routers.users import router as users_router
from fastapi_service.routers.items import router as items_router
from fastapi_service.routers.etl_orchestration import router as etl_router

from strawberry.fastapi import GraphQLRouter
import strawberry
from typing import List

from strawberry.fastapi import GraphQLRouter
from pydantic import BaseModel
from typing import List, Optional
import strawberry

# ---------------- FASTAPI APP ----------------
app = FastAPI(title="PyDataNova FastAPI v14")

origins = [
    "https://shadowwalkersb.github.io",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

# ---------------- MODELS ----------------
class User(BaseModel):
    id: int
    name: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_mock_router, prefix="/users-mock", tags=["users-mock"])
app.include_router(items_mock_router, prefix="/items-mock", tags=["items-mock"])
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(items_router, prefix="/items", tags=["items"])
app.include_router(etl_router, prefix="/etl", tags=["ETL"])

@app.get("/")
async def root():
    return {"message": "PyDataNova FastAPI Service running..."}

# ---------------- REST ENDPOINTS ----------------
@app.get("/")
async def root():
    return {"message": "Welcome to PyDataNova FastAPI v14"}

@app.get("/users")
def get_users():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

@app.get("/items")
def get_items():
    return [{"id": 101, "description": "Item A"}, {"id": 102, "description": "Item B"}]

@app.get("/pipeline/v14/run")
def run_pipeline():
    return {"status": "Pipeline started", "version": "v14"}

@app.get("/analytics/summary")
def analytics_summary():
    return {"users": 120, "items": 450, "sales": 9820.55}

@app.get("/ml/predict")
def ml_predict():
    return {"prediction": "class_A", "confidence": 0.87}

@app.post("/rpc/echo")
def rpc_echo(payload: Optional[dict] = None):
    return {"echo": payload or {"message": "hello"}}

@app.post("/image/face-detect")
def face_detect():
    return {"faces_detected": 3}

@app.post("/image/enhance")
def enhance_image():
    return {"status": "Image enhanced successfully"}

# ---------------- GRAPHQL ----------------
@strawberry.type
class UserType:
    id: int
    name: str

@strawberry.type
class ItemType:
    id: int
    description: str

@strawberry.type
class AnalyticsSummary:
    users: int
    items: int
    sales: float

@strawberry.type
class MLResult:
    prediction: str
    confidence: float

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello from FastAPI + GraphQL v14"

    @strawberry.field
    def top_users(self) -> List[UserType]:
        return [UserType(id=1, name="Alice"), UserType(id=2, name="Bob")]

    @strawberry.field
    def analytics_summary(self) -> AnalyticsSummary:
        return AnalyticsSummary(users=120, items=450, sales=9820.55)

    @strawberry.field
    def ml_query(self, input_text: str) -> MLResult:
        # simple dummy logic
        if "cat" in input_text.lower():
            return MLResult(prediction="cat", confidence=0.92)
        return MLResult(prediction="other", confidence=0.67)

# Create and mount GraphQL router
schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from fastapi import Response

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
