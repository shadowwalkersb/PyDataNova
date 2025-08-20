import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from fastapi import Request

logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Enable CORS so local frontend can fetch from backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logging.info(f"{request.method} {request.url}")
    response = await call_next(request)
    return response

@app.get("/")
def root():
    return {"message": "Hello from PyDataNova backend!"}

@app.get("/mock-data")
def mock_data():
    return {
        "columns": ["ID", "Value", "Category"],
        "rows": [
            [1, 42, "A"],
            [2, 17, "B"],
            [3, 33, "C"]
        ]
    }

@app.get("/status")
async def status():
    return {"status": "ok"}

# Optional: Use PORT from Render
port = int(os.environ.get("PORT", 10000))
