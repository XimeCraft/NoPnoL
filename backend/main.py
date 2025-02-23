from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

from .api import router
from .database import engine
from .models import Base

app = FastAPI(title="NoPnoL API")

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],  # Frontend server address
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ensure static directory exists
static_dir = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_dir, exist_ok=True)

print("Static directory:", os.path.exists(static_dir))  # 确保目录存在
print("Static directory path:", static_dir)  # 打印目录路径

# mount static files
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# register routes
app.include_router(router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to NoPnoL API"} 