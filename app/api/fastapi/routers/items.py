from fastapi import APIRouter, HTTPException, Query
from api.core.services import items as items_service
from api.core.utils.logger import get_logger
from api.core.utils.validation import validate_payload

logger = get_logger()
router = APIRouter()

@router.get("/")
async def get_items(db):
    logger.info(f"Fetching all items from {db}")
    return items_service.get_all_items(db)

@router.get("/{item_id}")
async def get_item(item_id, db):
    logger.info(f"Fetching item {item_id} from {db}")
    item = items_service.get_item_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/")
async def create_item(payload, db):
    try:
        validate_payload(["name", "owner_id"], payload)
        logger.info(f"Creating item in {db}: {payload}")
        return items_service.create_item(db, payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{item_id}")
async def update_item(item_id, payload, db):
    logger.info(f"Updating item {item_id} in {db} with {payload}")
    return items_service.update_item(db, item_id, payload)

@router.delete("/{item_id}")
async def delete_item(item_id, db):
    logger.info(f"Deleting item {item_id} from {db}")
    return items_service.delete_item(db, item_id)
