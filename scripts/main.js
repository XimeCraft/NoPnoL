// API Service
class API {
    static BASE_URL = 'http://localhost:8000/api';
    static IMAGE_BASE_URL = 'http://localhost:8000/';


    static async getCategories() {
        console.log('Attempting to fetch categories from:', `${this.BASE_URL}/categories`);
        try {
            const response = await fetch(`${this.BASE_URL}/categories`);
            if (!response.ok) throw new Error('Failed to fetch categories');

            const data = await response.json();
            console.log('Categories fetched successfully:', data);

            return data;
        } catch (error) {
            console.error('Error fetching categories:', error);
            throw error;
        }
    }

    static async getArticles(filter = 'all', page = 1, categoryId = null) {
        console.log('Attempting to fetch articles with params:', { filter, page, categoryId });
        try {
            const params = new URLSearchParams({
                filter,
                page: page.toString(),
                ...(categoryId && { category_id: categoryId.toString() })
            });
            console.log('Making request to:', `${this.BASE_URL}/articles?${params}`);

            const response = await fetch(`${this.BASE_URL}/articles?${params}`);
            if (!response.ok) throw new Error('Failed to fetch articles');

            const data = await response.json();
            console.log('Articles fetched successfully:', data);

            return data;

        } catch (error) {
            console.error('Error fetching articles:', error);
            throw error;
        }
    }
}

// UI Components
class CategoryList {
    constructor(container) {
        this.container = container;
        this.template = document.getElementById('categoryTemplate');
    }

    async render() {
        console.log("CategoryList render started");
        try {
            const categories = await API.getCategories();
            this.container.innerHTML = '';
            
            categories.forEach((category) => {
                const clone = this.template.content.cloneNode(true);
                const div = clone.querySelector('.category');
                const img = clone.querySelector('img');
                const span = clone.querySelector('span');

                const imageUrl = API.IMAGE_BASE_URL + category.image_url;
                img.src = imageUrl;
                img.alt = category.name;
                span.textContent = category.name;

                div.addEventListener('click', () => this.handleCategoryClick(div, category.id));
                
                this.container.appendChild(clone);
            });

            // Initialize articles
            await this.loadArticles();
        } catch (error) {
            console.error('Error rendering categories:', error);
        }
    }

    async handleCategoryClick(element, categoryId) {
        // Update selected state
        this.container.querySelectorAll('.category').forEach(cat => cat.classList.remove('active'));
        element.classList.add('active');

        // Reload articles
        await this.loadArticles();
    }

    async loadArticles() {
        try {
            const articleGrid = new ArticleGrid(document.getElementById('articleGrid'));
            await articleGrid.render('all', 1, null);
        } catch (error) {
            console.error('Error loading articles:', error);
        }
    }
}

class ArticleGrid {
    constructor(container) {
        this.container = container;
        this.template = document.getElementById('articleTemplate');
        this.currentPage = 1;
    }

    createTagElement(tagText, index) {
        const span = document.createElement('span');
        span.className = `tag tag-${(index % 3) + 1}`;
        span.textContent = `#${tagText}`;
        return span;
    }

    async render(filter = 'all', page = 1, categoryId = null) {
        try {
            const response = await API.getArticles(filter, page, categoryId);
            const articles = response.articles;
            
            if (page === 1) {
                this.container.innerHTML = '';
            }

            articles.forEach(article => {
                const clone = this.template.content.cloneNode(true);
                
                // Set article image
                clone.querySelector('.article-image img').src = API.IMAGE_BASE_URL + article.image_url;
                
                // Set author info
                clone.querySelector('.author-avatar').src = API.IMAGE_BASE_URL + article.author.avatar_url;
                clone.querySelector('.author-name').textContent = article.author.name;
                clone.querySelector('.author-profession').textContent = article.author.profession;
                
                // Set article details
                clone.querySelector('.publish-date').textContent = article.publish_date;
                clone.querySelector('.article-title').textContent = article.title;
                
                // Set tags
                const tagsContainer = clone.querySelector('.article-tags');
                article.tags.forEach((tag, index) => {
                    tagsContainer.appendChild(this.createTagElement(tag, index));
                });

                this.container.appendChild(clone);
            });

            // Update load more button state
            const loadMoreBtn = document.querySelector('.load-more');
            if (response.total <= page * response.limit) {
                loadMoreBtn.style.display = 'none';
            } else {
                loadMoreBtn.style.display = 'block';
            }

            this.currentPage = page;
        } catch (error) {
            console.error('Error rendering articles:', error);
        }
    }
}

// Initialize components
document.addEventListener('DOMContentLoaded', async () => {

    // Initialize Categories
    const categoryList = new CategoryList(document.getElementById('categoryContainer'));
    await categoryList.render();

    // Category Navigation
    const categoryContainer = document.querySelector('.category-container');
    const prevButton = document.querySelector('.category-nav.prev');
    const nextButton = document.querySelector('.category-nav.next');
    const scrollAmount = 200;

    prevButton.addEventListener('click', () => {
        categoryContainer.scrollBy({
            left: -scrollAmount,
            behavior: 'smooth'
        });
    });

    nextButton.addEventListener('click', () => {
        categoryContainer.scrollBy({
            left: scrollAmount,
            behavior: 'smooth'
        });
    });

    // Filter Buttons
    const filterButtons = document.querySelectorAll('.filter-btn');
    const articleGrid = new ArticleGrid(document.getElementById('articleGrid')); 
    
    filterButtons.forEach(button => {
        button.addEventListener('click', async () => {
            filterButtons.forEach(b => b.classList.remove('active'));
            button.classList.add('active');
            await articleGrid.render(button.dataset.filter, 1);
        });
    });

    // Load More Button
    const loadMoreButton = document.querySelector('.load-more');
    loadMoreButton.addEventListener('click', async () => {
        await articleGrid.render('all', articleGrid.currentPage + 1);
    });
}); 