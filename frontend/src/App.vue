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
  <Header />
  <Banner />
  <CategoryList @category-selected="handleCategorySelected" />
  <ArticleGrid :categoryId="selectedCategoryId" />
  <footer class="footer">
    <p>@2025 XimeCraft</p>
  </footer>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
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
  background-color: var(--bg-color);
  color: var(--primary-text);
  font-family: 'Inter', sans-serif;
  min-height: 100vh;
}

.footer {
  text-align: center;
  padding: 30px 0;
  font-family: 'Anta', sans-serif;
  font-size: 16px;
}
</style>
