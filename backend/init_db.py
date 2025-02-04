from backend.models.models import Base, Category, Article, Author, Tag
from backend.database import engine, SessionLocal
from datetime import datetime

def init_db():
    # create all tables
    Base.metadata.create_all(bind=engine)
    
    # create database session
    db = SessionLocal()
    
    try:
        # check if data already exists
        if db.query(Category).first() is None:
            # add sample category
            category = Category(
                name="CATEGORY1",
                image_url="/static/img/category1.png"
            )
            db.add(category)
            
            # add sample author
            author = Author(
                name="Xiao Meng",
                profession="Data Scientist",
                avatar_url="/static/img/authors/portfile.jpg"
            )
            db.add(author)
            
            # 添加示例标签
            tags = [
                Tag(name="Bias"),
                Tag(name="StatisticalBias"),
                Tag(name="DataBias")
            ]
            for tag in tags:
                db.add(tag)
            
            db.commit()
            
            # add sample article
            article = Article(
                title="AI is a Mirror: Machine Learning Learns the Human Bias",
                image_url="/static/img/articles/a1.jpg",
                publish_date=datetime.utcnow(),
                author=author,
                category=category,
                tags=tags
            )
            db.add(article)
            
            db.commit()
            print("Database initialized with sample data")
        else:
            print("Database already contains data")
            
    except Exception as e:
        print(f"Error initializing database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_db() 