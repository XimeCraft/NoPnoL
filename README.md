# NoPnoL - No Prejudice No Label

## Introduction

NoPnoL aims to address the inherent bias in machine learning models that often emerges from imbalanced real-world data distributions. While ML models strive for accuracy by fitting to real-world patterns, these patterns may perpetuate existing societal biases. This platform seeks to bridge the gap between "precise reality fitting" and "active fairness promotion" by providing objective, statistics-based analysis of potentially biased topics.

Although finding the perfect balance between these two goals remains challenging, we believe it's crucial to at least make visible what we might be sacrificing in pursuit of model accuracy.

## Current Status

**Branch**: `feat/notebook_page`
**Status**: Main page completed, Notebook page in planning

### Implemented Features ✅

#### Main Page
- **Category Navigation**: Horizontal scrollable category selector with smooth navigation arrows
- **Article Grid**: Responsive 3-column grid (adapts to 2 columns on tablets, 1 column on mobile)
- **Filtering System**: All/Latest/Popular filter tabs with active state highlighting
- **Pagination**: "Load More" button for incremental article loading
- **Article Cards**: Display author avatar, publication date, title, and color-coded tags
- **Responsive Design**: Full mobile and tablet support with breakpoints at 768px and 1200px
- **Modern UI**: Dark theme with gradient accents and smooth transitions

#### Backend API
- Category management endpoints
- Article CRUD operations with pagination
- Category-based filtering
- Tag system with many-to-many relationships
- Static file serving for images

### In Progress 🚧
- Notebook page (detailed article view)
- MVP roadmap planning

### Planned Features 📋
See [MVP_ROADMAP.md](MVP_ROADMAP.md) for detailed feature planning and timeline.

## Technical Stack

### Frontend (Vue.js)
- **Framework**: Vue 3.2+ with Composition API
- **Build Tool**: Vite 2.9+
- **State Management**: Pinia (configured, minimal usage currently)
- **Routing**: Vue Router 4
- **HTTP Client**: Axios
- **Styling**: Modern CSS with CSS Variables for theming
- **Fonts**:
  - Anta (headings and logos)
  - Inter (body text)
  - Alumni Sans (secondary text)

### Backend (FastAPI)
- **Framework**: FastAPI 0.68+
- **ORM**: SQLAlchemy 1.4+
- **Database**: SQLite (development), PostgreSQL ready
- **CORS**: Configured for localhost:3000 and localhost:5500
- **Python Version**: 3.8+

### Development Setup

#### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

#### Backend Setup
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize database (optional - db included)
python backend/init_db.py

# Run backend server from project root
uvicorn backend.main:app --reload
```

Backend will be available at: http://localhost:8000
API documentation: http://localhost:8000/docs

#### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

Frontend will be available at: http://localhost:3000

## API Documentation

### Endpoints

#### Categories
```
GET /api/categories
```
Returns all available categories with their images.

**Response**: `Array<Category>`
```json
[
  {
    "id": 1,
    "name": "Technology",
    "image_url": "static/categories/tech.jpg"
  }
]
```

#### Articles
```
GET /api/articles?page=1&category_id=1&filter=all
```
Get paginated articles with optional filtering.

**Query Parameters**:
- `page` (optional): Page number, default 1
- `limit` (optional): Items per page, default 9
- `category_id` (optional): Filter by category
- `filter` (optional): all | latest | popular

**Response**: `Array<Article>`
```json
[
  {
    "id": 1,
    "title": "Article Title",
    "image_url": "static/articles/article1.jpg",
    "content": "Article content...",
    "publish_date": "2025-01-02T00:00:00",
    "author": {
      "id": 1,
      "name": "Author Name",
      "profession": "Data Scientist",
      "avatar_url": "static/authors/avatar1.jpg"
    },
    "category_id": 1,
    "tags": ["Python", "AI", "Ethics"]
  }
]
```

#### Single Article
```
GET /api/articles/{article_id}
```
Get detailed information for a specific article.

**Response**: `Article`

#### Create Article
```
POST /api/articles
```
Create a new article (admin function).

**Request Body**: `ArticleCreate`
```json
{
  "title": "New Article",
  "content": "Content here...",
  "image_url": "static/articles/new.jpg",
  "author_id": 1,
  "category_id": 2,
  "tags": ["tag1", "tag2"]
}
```

## Database Schema

### Models

#### Category
- `id`: Integer, Primary Key
- `name`: String(50), Unique
- `image_url`: String(200)

#### Author
- `id`: Integer, Primary Key
- `name`: String(100)
- `profession`: String(100)
- `avatar_url`: String(200)

#### Article
- `id`: Integer, Primary Key
- `title`: String(200)
- `content`: Text
- `image_url`: String(200)
- `publish_date`: DateTime
- `author_id`: Foreign Key → Author
- `category_id`: Foreign Key → Category
- `tags`: Many-to-Many → Tag

#### Tag
- `id`: Integer, Primary Key
- `name`: String(50), Unique

#### article_tags (Junction Table)
- `article_id`: Foreign Key → Article
- `tag_id`: Foreign Key → Tag

## Project Structure

```
NoPnoL/
├── frontend/                    # Vue 3 frontend application
│   ├── src/
│   │   ├── components/          # Vue components
│   │   │   ├── Header.vue       # Navigation header with search and login
│   │   │   ├── Banner.vue       # Hero banner section
│   │   │   ├── CategoryList.vue # Category selector with navigation
│   │   │   └── ArticleGrid.vue  # Article grid with filtering
│   │   ├── router/              # Vue Router configuration
│   │   │   └── index.js
│   │   ├── stores/              # Pinia state stores
│   │   │   └── counter.js
│   │   ├── assets/              # Static assets and styles
│   │   │   ├── base.css
│   │   │   └── main.css
│   │   ├── App.vue              # Root component
│   │   └── main.js              # Application entry point
│   ├── package.json
│   ├── vite.config.js
│   └── index.html
│
├── backend/                     # FastAPI backend application
│   ├── __init__.py
│   ├── main.py                  # FastAPI app initialization, CORS, static files
│   ├── api.py                   # API route definitions
│   ├── models.py                # SQLAlchemy ORM models
│   ├── schemas.py               # Pydantic request/response schemas
│   ├── crud.py                  # Database CRUD operations
│   ├── database.py              # Database connection and session
│   ├── init_db.py               # Database initialization script
│   └── static/                  # Static files (images)
│       ├── categories/
│       ├── articles/
│       └── authors/
│
├── requirements.txt             # Python dependencies
├── nopnol.db                    # SQLite database
├── README.md                    # This file
├── MVP_ROADMAP.md              # Product roadmap and planning
└── .gitignore
```

## Component Architecture

### Header Component
- Navigation menu toggle (UI placeholder)
- NoPnoL logo
- Search bar (UI placeholder)
- Login button (UI placeholder)

### Banner Component
- Hero section with background image
- Mission statement display

### CategoryList Component
- Fetches categories from API
- Horizontal scrolling with navigation arrows
- Category selection with visual feedback
- Emits category selection events to parent

### ArticleGrid Component
- Receives category filter from parent
- Manages article fetching with pagination
- Filter tabs (All/Latest/Popular)
- Responsive grid layout
- "Load More" pagination
- Article cards with author info, date, tags

## Styling & Theme

### CSS Variables (Customizable)
```css
--bg-color: #000101              /* Main background */
--highlight-color: #87af20       /* Accent color */
--primary-text: #ffffff          /* Primary text */
--searchbar-color: #312f2f       /* Input backgrounds */
--selected-filter: #009970       /* Active filter/tab */
--category-bg-selected: #87af20  /* Selected category */
--category-bg-unselected: #312F2F /* Unselected category */
--tag-color-1: #FF1CF7          /* Tag color 1 */
--tag-color-2: #796EFF          /* Tag color 2 */
--tag-color-3: #40BBFD          /* Tag color 3 */
--button-gradient: linear-gradient(90deg, #FF38FF, #5C24FF, #2F85D9, #01E6B3)
```

### Responsive Breakpoints
- Mobile: < 768px (1 column grid)
- Tablet: 768px - 1200px (2 column grid)
- Desktop: > 1200px (3 column grid)

## Contributing

This project is in active development. See [MVP_ROADMAP.md](MVP_ROADMAP.md) for upcoming features and how to contribute.

## License

Copyright @2025 XimeCraft

