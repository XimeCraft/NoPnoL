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

        # Articles - Creating 15 sample articles
        articles = [
            Article(
                title="Getting Started with FastAPI",
                content="FastAPI is a modern web framework for building APIs with Python...",
                image_url="/static/img/articles/a1.jpg",
                category_id=1,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="Modern Web Design Principles",
                content="In today's digital landscape, web design plays a crucial role...",
                image_url="/static/img/articles/a1.jpg",
                category_id=2,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="Building Scalable APIs with Python",
                content="Learn how to build scalable and maintainable APIs using Python best practices...",
                image_url="/static/img/articles/a1.jpg",
                category_id=1,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="Understanding Machine Learning Bias",
                content="Exploring the challenges and implications of bias in ML models...",
                image_url="/static/img/articles/a1.jpg",
                category_id=4,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="Frontend Development Best Practices",
                content="A comprehensive guide to modern frontend development techniques...",
                image_url="/static/img/articles/a1.jpg",
                category_id=3,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="The Future of AI Ethics",
                content="Discussing the ethical implications and future of artificial intelligence...",
                image_url="/static/img/articles/a1.jpg",
                category_id=4,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="Responsive Design Patterns",
                content="Creating beautiful, responsive interfaces that work on all devices...",
                image_url="/static/img/articles/a1.jpg",
                category_id=2,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="Database Optimization Techniques",
                content="Improving database performance with proven optimization strategies...",
                image_url="/static/img/articles/a1.jpg",
                category_id=1,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="Neural Networks Explained",
                content="A beginner-friendly introduction to neural networks and deep learning...",
                image_url="/static/img/articles/a1.jpg",
                category_id=4,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="CSS Grid Layout Mastery",
                content="Master CSS Grid and create complex layouts with ease...",
                image_url="/static/img/articles/a1.jpg",
                category_id=2,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="API Security Best Practices",
                content="Protecting your APIs from common security vulnerabilities...",
                image_url="/static/img/articles/a1.jpg",
                category_id=1,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="Vue.js Component Design",
                content="Building reusable and maintainable Vue.js components...",
                image_url="/static/img/articles/a1.jpg",
                category_id=3,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="Fairness in Algorithmic Decision Making",
                content="Examining fairness metrics and their implications in AI systems...",
                image_url="/static/img/articles/a1.jpg",
                category_id=4,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="Microservices Architecture Guide",
                content="Designing and implementing microservices-based applications...",
                image_url="/static/img/articles/a1.jpg",
                category_id=3,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="Color Theory for UI Design",
                content="Understanding color psychology and creating harmonious color schemes...",
                image_url="/static/img/articles/a1.jpg",
                category_id=2,
                author_id=1,
                publish_date=datetime.now()
            ),
        ]

        # Add tags to articles
        articles[0].tags.extend([tags[0], tags[1]])  # Python, FastAPI
        articles[1].tags.extend([tags[2], tags[3]])  # Web Design, Frontend
        articles[2].tags.extend([tags[0], tags[1]])  # Python, FastAPI
        articles[3].tags.extend([tags[0]])  # Python
        articles[4].tags.extend([tags[3]])  # Frontend
        articles[5].tags.extend([tags[0]])  # Python
        articles[6].tags.extend([tags[2], tags[3]])  # Web Design, Frontend
        articles[7].tags.extend([tags[0]])  # Python
        articles[8].tags.extend([tags[0]])  # Python
        articles[9].tags.extend([tags[2], tags[3]])  # Web Design, Frontend
        articles[10].tags.extend([tags[0], tags[1]])  # Python, FastAPI
        articles[11].tags.extend([tags[3]])  # Frontend
        articles[12].tags.extend([tags[0]])  # Python
        articles[13].tags.extend([tags[0], tags[1]])  # Python, FastAPI
        articles[14].tags.extend([tags[2], tags[3]])  # Web Design, Frontend

        db.add_all(articles)
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