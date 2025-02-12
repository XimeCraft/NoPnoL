from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

from .api.endpoints import articles, categories
from .database import engine
from .models.models import Base

app = FastAPI(title="NoPnoL API")

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],  # 前端服务器地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ensure static directory exists
static_dir = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_dir, exist_ok=True)

# mount static files
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# register routes
app.include_router(articles.router, prefix="/api", tags=["articles"])
app.include_router(categories.router, prefix="/api", tags=["categories"])

@app.get("/")
async def root():
    return {"message": "Welcome to NoPnoL API"} 