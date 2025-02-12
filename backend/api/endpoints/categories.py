from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ...crud.crud import CategoryCRUD
from ...schemas import schemas
from ...database import get_db

router = APIRouter()

@router.get("/categories", response_model=List[schemas.CategoryResponse])
async def get_categories(db: Session = Depends(get_db)):
    return CategoryCRUD.get_all(db)

@router.post("/categories", response_model=schemas.CategoryResponse)
async def create_category(
    category: schemas.CategoryCreate,
    db: Session = Depends(get_db)
):
    return CategoryCRUD.create(db, category) 