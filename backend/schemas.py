from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class Category(BaseModel):
    id: int
    name: str
    image_url: Optional[str] = None

    class Config:
        from_attributes = True

class Author(BaseModel):
    id: int
    name: str
    profession: Optional[str] = None
    avatar_url: Optional[str] = None

    class Config:
        from_attributes = True

# Article schemas
class ArticleBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    content: str
    category_id: int = Field(..., gt=0)
    author_id: int = Field(..., gt=0)
    image_url: Optional[str] = None
    publish_date: datetime
    
class ArticleCreate(ArticleBase):
    tag_id: List[int] = []

class ArticleResponse(BaseModel):
    id: int
    title: str
    content: str
    publish_date: datetime
    author: Author
    category: Category
    tags: List[str]

    class Config:
        from_attributes = True 