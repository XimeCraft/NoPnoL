<!-- CategoryList.vue -->
<template>
  <section class="categories">
    <button class="category-nav prev" @click="scrollCategories('prev')">
      <span class="arrow-left"></span>
    </button>
    <div class="category-container" ref="containerRef">
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

const emit = defineEmits(['category-selected'])

const categories = ref([])
const selectedCategoryId = ref(null)
const containerRef = ref(null)

const API_BASE_URL = 'http://localhost:8000'

const getImageUrl = (path) => {
  if (!path) return ''
  return `${API_BASE_URL}${path.startsWith('/') ? path : '/' + path}`
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
  const container = document.querySelector('.category-container')
  if (!container) {
    console.error('Category container not found')
    return
  }

  const scrollAmount = 300
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
  padding: 0 120px 0 80px;
  margin-bottom: 50px;
  max-width: 1400px;
  margin-left: auto;
  margin-right: auto;
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
  left: 0px;
}

.category-nav.next {
  right: 30px;
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