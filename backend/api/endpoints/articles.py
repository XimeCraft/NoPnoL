from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from ...crud.crud import ArticleCRUD
from ...schemas import schemas
from ...database import get_db

router = APIRouter()

@router.get("/articles", response_model=List[schemas.ArticleResponse])
async def get_articles(
    filter: str = "all",
    page: int = Query(1, ge=1),
    limit: int = Query(12, ge=1, le=100),
    category_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    skip = (page - 1) * limit
    articles = ArticleCRUD.get_all(
        db=db,
        skip=skip,
        limit=limit,
        filter=filter,
        category_id=category_id
    )
    return articles

@router.get("/articles/{article_id}", response_model=schemas.ArticleResponse)
async def get_article(article_id: int, db: Session = Depends(get_db)):
    article = ArticleCRUD.get_by_id(db, article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.post("/articles", response_model=schemas.ArticleResponse)
async def create_article(
    article: schemas.ArticleCreate,
    db: Session = Depends(get_db)
):
    return ArticleCRUD.create(db, article) 