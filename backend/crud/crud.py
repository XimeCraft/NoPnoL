from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.models import Category, Article, Author, Tag
from ..schemas import schemas

class CategoryCRUD:
    @staticmethod
    def create(db: Session, category: schemas.CategoryCreate) -> Category:
        db_category = Category(**category.dict())
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category

    @staticmethod
    def get_all(db: Session) -> List[Category]:
        return db.query(Category).all()

class ArticleCRUD:
    @staticmethod
    def create(db: Session, article: schemas.ArticleCreate) -> Article:
        # 创建文章
        article_data = article.dict(exclude={'tag_names'})
        db_article = Article(**article_data)
        
        # 处理标签
        for tag_name in article.tag_names:
            # 查找或创建标签
            tag = db.query(Tag).filter(Tag.name == tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                db.add(tag)
            db_article.tags.append(tag)
        
        db.add(db_article)
        db.commit()
        db.refresh(db_article)
        return db_article

    @staticmethod
    def get_all(
        db: Session,
        skip: int = 0,
        limit: int = 12,
        filter: str = "all",
        category_id: Optional[int] = None
    ) -> List[Article]:
        query = db.query(Article)
        
        # 应用过滤器
        if filter == "latest":
            query = query.order_by(Article.publish_date.desc())
        elif filter == "popular":
            # 这里可以添加popularity的逻辑
            pass
            
        # 应用分类过滤
        if category_id:
            query = query.filter(Article.category_id == category_id)
        
        # 应用分页
        articles = query.offset(skip).limit(limit).all()
        return articles

    @staticmethod
    def get_by_id(db: Session, article_id: int) -> Optional[Article]:
        return db.query(Article).filter(Article.id == article_id).first()

class AuthorCRUD:
    @staticmethod
    def create(db: Session, author: schemas.AuthorCreate) -> Author:
        db_author = Author(**author.dict())
        db.add(db_author)
        db.commit()
        db.refresh(db_author)
        return db_author

    @staticmethod
    def get_by_id(db: Session, author_id: int) -> Optional[Author]:
        return db.query(Author).filter(Author.id == author_id).first() 