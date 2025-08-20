from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/root")
def root():
    return {"message": "Hello from FastAPI!"}

@app.get("/mock-data")
def mock_data():
    return {"data": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}
