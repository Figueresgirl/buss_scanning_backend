from fastapi import APIRouter
from backend.services.db import table

router = APIRouter()

@router.get("/inventory/list")
def list_inventory():
    try:
        response = table.scan()

        items = response.get("Items", [])

        return {
            "count": len(items),
            "items": items
        }

    except Exception as e:
        return {
            "error": str(e)
        }