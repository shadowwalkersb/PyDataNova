from fastapi import APIRouter, HTTPException, Query
from api.core.services import users as users_service
from api.core.utils.logger import get_logger
from api.core.utils.validation import validate_payload

logger = get_logger()
router = APIRouter()

@router.get("/")
async def get_users(db):
    logger.info(f"Fetching all users from {db}")
    return users_service.get_all_users(db)

@router.get("/{user_id}")
async def get_user(user_id, db):
    logger.info(f"Fetching user {user_id} from {db}")
    user = users_service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/")
async def create_user(payload: dict, db: str = Query(...)):
    try:
        validate_payload(["name", "email"], payload)
        logger.info(f"Creating user in {db}: {payload}")
        return users_service.create_user(db, payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{user_id}")
async def update_user(user_id: int, payload: dict, db: str = Query(...)):
    logger.info(f"Updating user {user_id} in {db} with {payload}")
    return users_service.update_user(db, user_id, payload)

@router.delete("/{user_id}")
async def delete_user(user_id: int, db: str = Query(...)):
    logger.info(f"Deleting user {user_id} from {db}")
    return users_service.delete_user(db, user_id)
