from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/")
def products_list():
    return [{"id": 1, "name": "Pen"}]