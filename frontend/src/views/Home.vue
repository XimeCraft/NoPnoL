<script setup>
import { ref } from 'vue'
import Header from '../components/Header.vue'
import Banner from '../components/Banner.vue'
import CategoryList from '../components/CategoryList.vue'
import ArticleGrid from '../components/ArticleGrid.vue'

const selectedCategoryId = ref(null)

const handleCategorySelected = (categoryId) => {
  selectedCategoryId.value = categoryId
}
</script>

<template>
  <div class="home-container">
    <Header />
    <Banner />
    <CategoryList @category-selected="handleCategorySelected" />
    <ArticleGrid :categoryId="selectedCategoryId" />
    <footer class="footer">
      <p>@2025 XimeCraft</p>
    </footer>
  </div>
</template>

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.footer {
  position: relative;
  text-align: center;
  padding: 200px 0 100px 0;
  font-family: 'Anta', sans-serif;
  font-size: 16px;
  width: 100%;
  min-height: 400px;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  z-index: 1;
}

.footer p {
  position: relative;
  z-index: 1;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
}
</style>
