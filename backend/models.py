from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# article-tag relation table
article_tags = Table(
    'article_tags',
    Base.metadata,
    Column('article_id', Integer, ForeignKey('articles.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    image_url = Column(String(200), nullable=False)

    articles = relationship('Article', back_populates='category')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'image_url': self.image_url
        }

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    profession = Column(String(100))
    avatar_url = Column(String(200))

    articles = relationship('Article', back_populates='author')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'profession': self.profession,
            'avatar_url': self.avatar_url
        }

class Tag(Base):
    __tablename__ = 'tags'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Article(Base):
    __tablename__ = 'articles'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    image_url = Column(String(200))
    content = Column(Text)
    publish_date = Column(DateTime, default=datetime.now)
    author_id = Column(Integer, ForeignKey('authors.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    author = relationship('Author', back_populates='articles')
    category = relationship('Category', back_populates='articles')
    tags = relationship('Tag', secondary=article_tags)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,  
            'content': self.content,
            'image_url': self.image_url,
            'publish_date': self.publish_date,
            'author': self.author.to_dict() if self.author else None,
            'category': self.category.to_dict() if self.category else None,
            'tags': [tag.name for tag in self.tags]
        } 