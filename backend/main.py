from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
import os

from .models.models import Category, Article, Author, Tag
from .database import SessionLocal, engine

app = FastAPI(title="NoPnoL API")

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],  # 前端服务器地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ensure static directory exists
static_dir = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_dir, exist_ok=True)

# mount static files
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Welcome to NoPnoL API"}

@app.get("/api/categories")
async def get_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    return [category.to_dict() for category in categories]

@app.get("/api/articles")
async def get_articles(
    filter: str = "all",
    page: int = Query(1, ge=1),
    limit: int = Query(12, ge=1, le=100),
    category_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    # base query
    query = db.query(Article)
    
    # apply filter
    if filter == "latest":
        query = query.order_by(Article.publish_date.desc())
    elif filter == "popular":
        pass
        
    # apply category filter
    if category_id:
        query = query.filter(Article.category_id == category_id)
    
    # calculate pagination
    total = query.count()
    articles = query.offset((page - 1) * limit).limit(limit).all()
    
    return {
        "total": total,
        "page": page,
        "limit": limit,
        "articles": [article.to_dict() for article in articles]
    }

@app.get("/api/articles/{article_id}")
async def get_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article.to_dict() 