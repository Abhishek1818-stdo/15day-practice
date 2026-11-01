from fastapi import FastAPI
from routers.users import router as users_router
from routers.products import router as products_router

app = FastAPI()

app.include_router(users_router, prefix="/api/v1")
app.include_router(products_router, prefix="/api/v1")