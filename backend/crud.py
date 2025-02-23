from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List, Optional
from . import models, schemas
from datetime import datetime

class ArticleCRUD:
    @staticmethod
    def get_articles(db: Session, page_number: int = 1, limit: int = 9, category_id: Optional[int] = None) -> List[models.Article]:
        """Get all articles with pagination and category filtering"""
        query = db.query(models.Article)        

        if category_id:
            query = query.filter(models.Article.category_id == category_id)
        skip = (page_number - 1) * limit
        articles = query.order_by(desc(models.Article.publish_date)).offset(skip).limit(limit).all()
        
        return [article.to_dict() for article in articles]


    @staticmethod
    def get_article(db: Session, article_id: int) -> Optional[models.Article]:
        article = db.query(models.Article).filter(models.Article.id == article_id).first()
        return article.to_dict()

    @staticmethod
    def create_article(db: Session, article: schemas.ArticleCreate) -> models.Article:
        db_article = models.Article(
            title=article.title,
            image_url=article.image_url,
            content=article.content,
            category_id=article.category_id,
            author_id=article.author_id,
            publish_date=article.publish_date
        )
        db.add(db_article)
        db.commit()
        db.refresh(db_article)

        # check tags are existing
        tags = db.query(models.Tag).filter(models.Tag.id.in_(article.tag_ids)).all()

        # Add tags to the article_tag mapping table
        db_article.tags = tags

        db.commit()
        return db_article
    
class CategoryCRUD:
    @staticmethod
    def get_categories(db: Session) -> List[models.Category]:
        query = db.query(models.Category)
        return query.order_by(models.Category.id).all()
