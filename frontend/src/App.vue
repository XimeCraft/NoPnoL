<script setup>
import { ref } from 'vue'
import Header from './components/Header.vue'
import Banner from './components/Banner.vue'
import CategoryList from './components/CategoryList.vue'
import ArticleGrid from './components/ArticleGrid.vue'

const selectedCategoryId = ref(null)

const handleCategorySelected = (categoryId) => {
  selectedCategoryId.value = categoryId
}
</script>

<template>
  <div class="app-container">
    <Header />
    <Banner />
    <CategoryList @category-selected="handleCategorySelected" />
    <ArticleGrid :categoryId="selectedCategoryId" />
    <footer class="footer">
      <p>@2025 XimeCraft</p>
    </footer>
  </div>
</template>

<style>
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  width: 100vw;
  max-width: 100%;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}

:root {
  /* General Colors */
  --bg-color: #000101;
  --highlight-color: #87af20;
  --primary-text: #ffffff;
  --searchbar-color: #312f2f;
  --selected-filter: #01e6b3;

  /* Category Colors */
  --category-bg-selected: #87af20;
  --category-bg-unselected: #312F2F;
  --category-arrow-bg: #312F2F;

  /* Tag Colors */
  --tag-color-1: #FF1CF7;
  --tag-color-2: #796EFF;
  --tag-color-3: #40BBFD;

  /* Load More Button Gradient */
  --button-gradient: linear-gradient(90deg, #FF38FF, #5C24FF, #2F85D9, #01E6B3);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
  background-color: var(--bg-color);
  color: var(--primary-text);
  font-family: 'Inter', sans-serif;
  min-height: 100vh;
  width: 100vw;
  overflow-x: hidden;
}

.footer {
  text-align: center;
  padding: 30px 0;
  font-family: 'Anta', sans-serif;
  font-size: 16px;
  width: 100%;
}
</style>
