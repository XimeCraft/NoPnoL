from datetime import datetime
from database import engine, SessionLocal
from models import Base, Category, Author, Article, Tag

# 创建所有表
def init_db():
    Base.metadata.create_all(bind=engine)

def init_data():
    db = SessionLocal()
    try:
        # 清空现有数据
        print("Clearing existing data...")
        db.query(Article).delete()
        db.query(Tag).delete()
        db.query(Category).delete()
        db.query(Author).delete()
        db.commit()

        # Categories
        categories = [
            Category(name="Technology", image_url="/static/img/categories/Technology.png"),
            Category(name="Design", image_url="/static/img/categories/Design.png"),
            Category(name="Development", image_url="/static/img/categories/Development.png"),
            Category(name="AI", image_url="/static/img/categories/AI.jpg")
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
                title="AI is a Mirror: Machine Learning Learns the Human Bias",
                content="FastAPI is a modern web framework for building APIs with Python...",
                image_url="/static/img/articles/a1.jpg",
                category_id=1,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="AI is a Mirror: Machine Learning Learns the Human Bias",
                content="In today's digital landscape, web design plays a crucial role...",
                image_url="/static/img/articles/a1.jpg",
                category_id=2,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="AI is a Mirror: Machine Learning Learns the Human Bias",
                content="Learn how to build scalable and maintainable APIs using Python best practices...",
                image_url="/static/img/articles/a1.jpg",
                category_id=1,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="AI is a Mirror: Machine Learning Learns the Human Bias",
                content="Exploring the challenges and implications of bias in ML models...",
                image_url="/static/img/articles/a1.jpg",
                category_id=4,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="AI is a Mirror: Machine Learning Learns the Human Bias",
                content="A comprehensive guide to modern frontend development techniques...",
                image_url="/static/img/articles/a1.jpg",
                category_id=3,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="AI is a Mirror: Machine Learning Learns the Human Bias",
                content="Discussing the ethical implications and future of artificial intelligence...",
                image_url="/static/img/articles/a1.jpg",
                category_id=4,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="AI is a Mirror: Machine Learning Learns the Human Bias",
                content="Creating beautiful, responsive interfaces that work on all devices...",
                image_url="/static/img/articles/a1.jpg",
                category_id=2,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="AI is a Mirror: Machine Learning Learns the Human Bias",
                content="Improving database performance with proven optimization strategies...",
                image_url="/static/img/articles/a1.jpg",
                category_id=1,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="AI is a Mirror: Machine Learning Learns the Human Bias",
                content="A beginner-friendly introduction to neural networks and deep learning...",
                image_url="/static/img/articles/a1.jpg",
                category_id=4,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="AI is a Mirror: Machine Learning Learns the Human Bias",
                content="Master CSS Grid and create complex layouts with ease...",
                image_url="/static/img/articles/a1.jpg",
                category_id=2,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="AI is a Mirror: Machine Learning Learns the Human Bias",
                content="Protecting your APIs from common security vulnerabilities...",
                image_url="/static/img/articles/a1.jpg",
                category_id=1,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="AI is a Mirror: Machine Learning Learns the Human Bias",
                content="Building reusable and maintainable Vue.js components...",
                image_url="/static/img/articles/a1.jpg",
                category_id=3,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="AI is a Mirror: Machine Learning Learns the Human Bias",
                content="Examining fairness metrics and their implications in AI systems...",
                image_url="/static/img/articles/a1.jpg",
                category_id=4,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="AI is a Mirror: Machine Learning Learns the Human Bias",
                content="Designing and implementing microservices-based applications...",
                image_url="/static/img/articles/a1.jpg",
                category_id=3,
                author_id=1,
                publish_date=datetime.now()
            ),
            Article(
                title="AI is a Mirror: Machine Learning Learns the Human Bias",
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