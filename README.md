# NoPnoL - No Prejudice No Label

## Introduction

NoPnoL aims to address the inherent bias in machine learning models that often emerges from imbalanced real-world data distributions. While ML models strive for accuracy by fitting to real-world patterns, these patterns may perpetuate existing societal biases. This platform seeks to bridge the gap between "precise reality fitting" and "active fairness promotion" by firstly, providing objective, statistics-based analysis of potentially biased topics.

Although finding the perfect balance between these two goals remains challenging, I believe it's crucial to at least make visible what we might be sacrificing in pursuit of model accuracy.


## Technical Overview

### Frontend (Vue.js)
- Vue 3 with Composition API
- Vite for build tooling
- Responsive design with modern CSS
- Component-based architecture
- Axios for API communication

### Backend (FastAPI)
- FastAPI framework
- SQLAlchemy ORM
- SQLite database
- RESTful API design
- Static file serving

### Development
```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

### API Endpoints
- `/api/categories` - Get all categories
- `/api/articles` - Get articles with filtering and pagination
- `/api/articles/{id}` - Get specific article details

### Database Schema
- Categories
- Articles
- Authors
- Tags
- Article-Tag relations

