<!-- ArticleGrid.vue -->
<template>
  <div>
    <section class="filters">
      <div class="filter-container">
        <button v-for="filter in filters"
                :key="filter.value"
                class="filter-btn"
                :class="{ active: currentFilter === filter.value }"
                @click="changeFilter(filter.value)">
          {{ filter.label }}
        </button>
      </div>
    </section>

    <main class="article-grid">
      <article v-for="article in articles" 
               :key="article.id" 
               class="article-card">
        <div class="article-image">
          <img :src="getImageUrl(article.image_url)" alt="Article">
        </div>
        <div class="article-content">
          <div class="article-author">
            <img :src="getImageUrl(article.author.avatar_url)" :alt="article.author.name" class="author-avatar">
            <div class="author-info">
              <span class="author-name">{{ article.author.name }}</span>
              <span class="author-profession">{{ article.author.profession }}</span>
            </div>
          </div>
          <time class="publish-date">{{ formatDate(article.publish_date) }}</time>
          <h3 class="article-title">{{ article.title }}</h3>
          <div class="article-tags">
            <span v-for="(tag, index) in article.tags" 
                  :key="tag"
                  class="tag"
                  :class="'tag-' + ((index % 3) + 1)">
              #{{ tag }}
            </span>
          </div>
        </div>
      </article>
    </main>

    <button v-if="hasMore" 
            class="load-more"
            @click="loadMore">
      Load More
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'

const props = defineProps({
  categoryId: {
    type: Number,
    default: null
  }
})

const API_BASE_URL = 'http://localhost:8000'
const articles = ref([])
const currentPage = ref(1)
const hasMore = ref(true)
const currentFilter = ref('all')

const filters = [
  { label: 'All', value: 'all' },
  { label: 'Latest', value: 'latest' },
  { label: 'Popular', value: 'popular' }
]

const getImageUrl = (path) => {
  return `${API_BASE_URL}${path}`
}

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

const fetchArticles = async (page = 1, filter = 'all', reset = false) => {
  try {
    const params = new URLSearchParams({
      page: page.toString(),
      filter,
      ...(props.categoryId && { category_id: props.categoryId.toString() })
    })

    const response = await axios.get(`${API_BASE_URL}/api/articles?${params}`)
    
    if (reset) {
      articles.value = response.data
    } else {
      articles.value = [...articles.value, ...response.data]
    }

    hasMore.value = response.data.length === 9 // 假设每页9条数据
    currentPage.value = page
  } catch (error) {
    console.error('Error fetching articles:', error)
  }
}

const loadMore = () => {
  fetchArticles(currentPage.value + 1, currentFilter.value)
}

const changeFilter = (filter) => {
  currentFilter.value = filter
  currentPage.value = 1
  fetchArticles(1, filter, true)
}

watch(() => props.categoryId, () => {
  currentPage.value = 1
  fetchArticles(1, currentFilter.value, true)
})

onMounted(() => {
  fetchArticles()
})
</script>

<style scoped>
.filters {
  display: flex;
  justify-content: flex-end;
  padding: 0 120px;
  margin-bottom: 50px;
}

.filter-container {
  display: flex;
  gap: 20px;
}

.filter-btn {
  padding: 10px 20px;
  border: none;
  border-radius: 20px;
  background-color: var(--category-bg-unselected);
  color: var(--primary-text);
  font-family: 'Anta', sans-serif;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: inset -4px -4px 8px rgba(255, 255, 255, 0.1),
              inset 4px 4px 8px rgba(0, 0, 0, 0.3);
}

.filter-btn.active {
  background-color: var(--selected-filter);
  box-shadow: none;
}

.article-grid {
  max-width: 1580px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 30px;
  padding: 0 20px;
  margin-bottom: 50px;
}

.article-card {
  width: 350px;
  height: 480px;
  background-color: var(--searchbar-color);
  border-radius: 15px;
  overflow: hidden;
}

.article-image {
  width: 326px;
  height: 228px;
  margin: 12px;
}

.article-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.article-content {
  padding: 20px;
}

.article-author {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 15px;
}

.author-avatar {
  width: 67px;
  height: 60px;
  border-radius: 10px;
  object-fit: cover;
}

.author-info {
  display: flex;
  flex-direction: column;
}

.author-name {
  font-family: 'Anta', sans-serif;
  font-size: 16px;
  font-weight: 400;
  color: var(--primary-text);
}

.author-profession {
  font-family: 'Alumni Sans', sans-serif;
  font-size: 16px;
  font-weight: 400;
  color: var(--primary-text);
  opacity: 0.8;
}

.publish-date {
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  font-weight: 600;
  color: var(--selected-filter);
  margin-bottom: 10px;
  display: block;
}

.article-title {
  font-family: 'Inter', sans-serif;
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 20px;
}

.article-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.tag {
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  padding: 5px 10px;
  border-radius: 15px;
  background-color: transparent;
}

.tag-1 { border: 1px solid var(--tag-color-1); color: var(--tag-color-1); }
.tag-2 { border: 1px solid var(--tag-color-2); color: var(--tag-color-2); }
.tag-3 { border: 1px solid var(--tag-color-3); color: var(--tag-color-3); }

.load-more {
  display: block;
  margin: 0 auto 50px;
  padding: 15px 40px;
  font-family: 'Anta', sans-serif;
  font-size: 18px;
  color: var(--primary-text);
  background: var(--button-gradient);
  border: none;
  border-radius: 25px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.load-more:hover {
  transform: scale(1.05);
}
</style> 