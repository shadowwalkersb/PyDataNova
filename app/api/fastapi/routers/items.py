from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_items():
    return [
        { "id": 1, "name": "Laptop", "category": "Electronics", "price": 999.99, "owner_id": 1 },
        { "id": 2, "name": "Desk Chair", "category": "Furniture", "price": 199.99, "owner_id": 2 },
        { "id": 3, "name": "Water Bottle", "category": "Accessories", "price": 14.99, "owner_id": 1 },
        { "id": 4, "name": "Notebook", "category": "Stationery", "price": 3.49, "owner_id": 3 },
        { "id": 5, "name": "Headphones", "category": "Electronics", "price": 79.99, "owner_id": 2 }
        ]
