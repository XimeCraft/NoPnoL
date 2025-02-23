from datetime import datetime
from database import engine, SessionLocal
from models import Base, Category, Author, Article, Tag

# 创建所有表
def init_db():
    Base.metadata.create_all(bind=engine)

def init_data():
    db = SessionLocal()
    try:
        # Categories
        categories = [
            Category(name="Technology", image_url="/static/img/categories/category1.jpg"),
            Category(name="Design", image_url="/static/img/categories/category1.jpg"),
            Category(name="Development", image_url="/static/img/categories/category1.jpg"),
            Category(name="AI", image_url="/static/img/categories/category1.jpg")
        ]
        db.add_all(categories)
        db.commit()

        # Authors
        authors = [
            Author(
                name="Xiao MENG",
                profession="Data Scientist",
                avatar_url="/static/img/authors/author1.jpg"
            )
        ]
        db.add_all(authors)
        db.commit()

        # Tags
        tags = [
            Tag(name="Python"),
            Tag(name="FastAPI"),
            Tag(name="Web Design"),
            Tag(name="Frontend")
        ]
        db.add_all(tags)
        db.commit()

        # Articles
        article1 = Article(
            title="Getting Started with FastAPI",
            content="FastAPI is a modern web framework for building APIs with Python...",
            image_url="/static/img/articles/a1.jpg",
            category_id=1, 
            author_id=1,    
            publish_date=datetime.now()
        )
        article1.tags.extend([tags[0], tags[1]])  # Python, FastAPI

        article2 = Article(
            title="Modern Web Design Principles",
            content="In today's digital landscape, web design plays a crucial role...",
            image_url="/static/img/articles/a1.jpg",
            category_id=2,  
            author_id=1,    
            publish_date=datetime.now()
        )
        article2.tags.extend([tags[1], tags[2], tags[3]])  # Web Design, Frontend

        db.add_all([article1, article2])
        db.commit()

    except Exception as e:
        print(f"Error initializing data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("Creating database tables...")
    init_db()
    print("Tables created successfully!")
    
    print("Initializing sample data...")
    init_data()
    print("Sample data initialized successfully!") 