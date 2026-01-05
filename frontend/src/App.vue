<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <div class="app-container">
    <RouterView />
  </div>
</template>

<style>
.app-container {
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
  --selected-filter: #009970;

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

</style>
