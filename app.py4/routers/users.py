from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def users_list():
    return [{"id": 1, "name": "Sam"}]