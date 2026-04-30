from fastapi import APIRouter
from backend.services.llm_parser import extract_items

router = APIRouter()

@router.get("/test")
def test():
    return {"message": "Router is working"}

@router.post("/scan")
def scan(data: dict):
    text = data.get("text", "")

    if not text:
        return {"error": "No text provided"}

    result = extract_items(text)

    return {
        "message": "Scan successful",
        "data": result
    }