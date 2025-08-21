from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_users():
    return [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Doe"}]
