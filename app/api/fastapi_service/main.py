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
import strawberry
from typing import List

app = FastAPI(title="FastAPI Service")

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

app.include_router(users_mock_router, prefix="/users-mock", tags=["users-mock"])
app.include_router(items_mock_router, prefix="/items-mock", tags=["items-mock"])
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(items_router, prefix="/items", tags=["items"])
app.include_router(etl_router, prefix="/etl", tags=["ETL"])

@app.get("/")
async def root():
    return {"message": "PyDataNova FastAPI Service running..."}

# ---------------- REST ENDPOINTS ----------------
@app.get("/analytics/summary")
def analytics_summary():
    return {"summary": {"users": 123, "events": 456, "sales": 789}}

@app.get("/ml/predict")
def ml_predict():
    return {"prediction": "class_A", "confidence": 0.92}

@app.get("/rpc/echo")
def rpc_echo(msg: str = "hello"):
    return {"echo": msg}

# ---------------- GRAPHQL ----------------
@strawberry.type
class AnalyticsSummary:
    mean: float
    std: float


@strawberry.type
class MLResult:
    prediction: str
    confidence: float

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello from GraphQL"

    @strawberry.field
    def top_users(self) -> List[str]:
        return ["alice", "bob", "charlie"]

    @strawberry.field
    def analytics_summary(self) -> AnalyticsSummary:
        # Mock numbers — replace later with real DB/statistics
        return AnalyticsSummary(mean=42.0, std=3.14)

    @strawberry.field
    def ml_query(self, input_text: str) -> MLResult:
        """
        Example ML query. Replace with actual model call.
        """
        # mock logic
        if "cat" in input_text.lower():
            return MLResult(prediction="cat", confidence=0.92)
        else:
            return MLResult(prediction="other", confidence=0.67)

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

# --- Mount GraphQL route ---
app.include_router(graphql_app, prefix="/graphql")
