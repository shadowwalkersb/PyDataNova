from fastapi import FastAPI

app = FastAPI(title="PyDataNova FastAPI v6")

@app.get("/")
async def root():
    return {"message": "Welcome to PyDataNova FastAPI v6"}
