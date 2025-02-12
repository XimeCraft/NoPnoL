from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./nopnol.db"
# 如果使用PostgreSQL:
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/nopnol"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # 仅用于SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 依赖项
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 