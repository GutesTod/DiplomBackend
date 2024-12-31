from fastapi import Depends
from app.core import get_session
from .base_service import BaseService
from app.models import Category
from sqlalchemy.ext.asyncio import AsyncSession

class CategoryService(BaseService[Category]):
    def __init__(self, db_session: AsyncSession):
        super().__init__(Category, db_session)
        

def get_category_service(
    db_session: AsyncSession = Depends(get_session),
) -> CategoryService:
    return CategoryService(db_session)