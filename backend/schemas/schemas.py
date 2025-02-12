from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Category schemas
class CategoryBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    image_url: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True

# Author schemas
class AuthorBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    profession: Optional[str] = None
    avatar_url: Optional[str] = None

class AuthorCreate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int

    class Config:
        from_attributes = True

# Tag schemas
class TagBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)

class TagCreate(TagBase):
    pass

class TagResponse(TagBase):
    id: int

    class Config:
        from_attributes = True

# Article schemas
class ArticleBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    image_url: Optional[str] = None
    category_id: int = Field(..., gt=0)
    author_id: int = Field(..., gt=0)

class ArticleCreate(ArticleBase):
    tag_names: List[str] = []

class ArticleResponse(BaseModel):
    id: int
    title: str
    image_url: Optional[str]
    publish_date: datetime
    author: AuthorResponse
    category: CategoryResponse
    tags: List[str]

    class Config:
        from_attributes = True 