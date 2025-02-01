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

// Category Selection
const categories = document.querySelectorAll('.category');
categories.forEach(category => {
    category.addEventListener('click', () => {
        categories.forEach(c => c.classList.remove('active'));
        category.classList.add('active');
    });
});

// Filter Selection
const filterButtons = document.querySelectorAll('.filter-btn');
filterButtons.forEach(button => {
    button.addEventListener('click', () => {
        filterButtons.forEach(b => b.classList.remove('active'));
        button.classList.add('active');
    });
});

// Load More Button (placeholder functionality)
const loadMoreButton = document.querySelector('.load-more');
loadMoreButton.addEventListener('click', () => {
    console.log('Load more content...');
    // Implement actual content loading logic here
}); 