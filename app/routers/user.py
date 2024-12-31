from fastapi import APIRouter, Depends

from app.schemas import UserSchemas
from app.services import UserService, get_user_service

user_router = APIRouter(prefix="/user", tags=["Пользователи"])

@user_router.get("/")
async def get_users(
    service: UserService = Depends(get_user_service)
):
    return await service.get()
    
@user_router.post("/")
async def create_user(
    data: UserSchemas.UserCreate,
    service: UserService = Depends(get_user_service)
):
    return await service.create(data=data)
    
@user_router.delete("/")
async def delete_user():
    ...
    
@user_router.patch("/")
async def update_user():
    ...