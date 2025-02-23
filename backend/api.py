from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from . import schemas, models
from .database import get_db
from .crud import ArticleCRUD, CategoryCRUD

router = APIRouter()

# Categories
@router.get("/categories", response_model=List[schemas.Category])
def get_categories(db: Session = Depends(get_db)):
    """Get all categories"""

    categories = CategoryCRUD.get_categories(db)
    return categories

# Articles
@router.get("/articles", response_model=List[schemas.ArticleResponse])
def get_articles(
    page_number: int = 1,
    limit: int = 9,
    category_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """Get articles with pagination and category filtering"""

    articles = ArticleCRUD.get_articles(db, page_number=page_number, limit=limit, category_id=category_id)
    return articles

@router.get("/articles/{article_id}", response_model=schemas.ArticleResponse)
def get_article(article_id: int, db: Session = Depends(get_db)):
    """Get a single article detail"""

    article = ArticleCRUD.get_article(db, article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.post("/articles", response_model=schemas.ArticleResponse)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    """Create a new article"""
    
    return ArticleCRUD.create_article(db, article) 