<!-- CategoryList.vue -->
<template>
  <section class="categories">
    <button class="category-nav prev" @click="scrollCategories('prev')">
      <span class="arrow-left"></span>
    </button>
    <div class="category-container">
      <div v-for="category in categories" 
           :key="category.id" 
           class="category"
           :class="{ active: selectedCategoryId === category.id }"
           @click="selectCategory(category)">
        <img :src="getImageUrl(category.image_url)" :alt="category.name">
        <span>{{ category.name }}</span>
      </div>
    </div>
    <button class="category-nav next" @click="scrollCategories('next')">
      <span class="arrow-right"></span>
    </button>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const categories = ref([])
const selectedCategoryId = ref(null)
const containerRef = ref(null)

const API_BASE_URL = 'http://localhost:8000'

const getImageUrl = (path) => {
  return `${API_BASE_URL}${path}`
}

const fetchCategories = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/api/categories`)
    categories.value = response.data
  } catch (error) {
    console.error('Error fetching categories:', error)
  }
}

const selectCategory = (category) => {
  selectedCategoryId.value = category.id
  // 触发事件通知父组件
  emit('category-selected', category.id)
}

const scrollCategories = (direction) => {
  const container = containerRef.value
  if (!container) return
  
  const scrollAmount = 200
  const scrollOffset = direction === 'prev' ? -scrollAmount : scrollAmount
  
  container.scrollBy({
    left: scrollOffset,
    behavior: 'smooth'
  })
}

onMounted(() => {
  fetchCategories()
})
</script>

<style scoped>
.categories {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 30px;
  margin-bottom: 50px;
}

.category-container {
  display: flex;
  gap: 20px;
  overflow-x: auto;
  scroll-behavior: smooth;
  -ms-overflow-style: none;
  scrollbar-width: none;
  padding: 10px;
  justify-content: center;
}

.category-container::-webkit-scrollbar {
  display: none;
}

.category {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  gap: 10px;
  width: 160px;
  height: 160px;
  padding: 15px;
  border-radius: 15px;
  background-color: var(--category-bg-unselected);
  cursor: pointer;
  transition: background-color 0.3s ease;
  flex-shrink: 0;
}

.category.active {
  background-color: var(--category-bg-selected);
}

.category img {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
  flex-shrink: 0;
}

.category span {
  font-family: 'Anta', sans-serif;
  font-size: 14px;
  text-align: center;
  max-width: 90%;
  word-wrap: break-word;
  min-height: 40px;
}

.category-nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%); 
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: var(--category-arrow-bg);
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
}

.category-nav.prev {
  left: 20px;
}

.category-nav.next {
  right: 20px;
}

.arrow-left, .arrow-right {
  width: 0;
  height: 0;
  border: solid var(--primary-text);
  border-width: 0 3px 3px 0;
  display: inline-block;
  padding: 4px;
}

.arrow-left {
  transform: rotate(135deg);
}

.arrow-right {
  transform: rotate(-45deg);
}
</style> 