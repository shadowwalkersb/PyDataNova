from fastapi import APIRouter, HTTPException, Query
from api.core.services import users as users_service

router = APIRouter()

@router.get("/")
async def get_users(db):
    return users_service.get_all_users(db)

@router.get("/{user_id}")
async def get_user(user_id, db):
    user = users_service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
