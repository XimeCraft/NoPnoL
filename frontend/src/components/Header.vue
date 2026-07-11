<!-- Header.vue -->
<template>
  <header class="header">
    <button class="nav-toggle">
      <span></span>
      <span></span>
      <span></span>
    </button>
    <h1 class="logo">NoPnoL</h1>
    <div class="search-container">
      <input type="search" class="search-bar" placeholder="Search...">
    </div>
    <div class="auth-buttons">
      <button class="signup-btn">Sign up</button>
      <button class="login-btn">Login</button>
    </div>
  </header>
</template>

<script setup>
</script>

<style scoped>
.header {
  display: flex;
  align-items: center;
  padding: 20px 50px;
  gap: 30px;
}

.nav-toggle {
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 10px;
}

.nav-toggle span {
  display: block;
  width: 30px;
  height: 3px;
  border-radius: 3px;
}

.nav-toggle span:nth-child(1) { background-color: #DF19D8; }
.nav-toggle span:nth-child(2) { background-color: #5c24ff; }
.nav-toggle span:nth-child(3) { background-color: #01e6b3; }

.logo {
  font-family: 'Anta', sans-serif;
  font-size: 52px;
  font-weight: 400;
  color: var(--primary-text);
}

.search-container {
  flex-grow: 1;
  display: flex;
  justify-content: center;
}

.search-bar {
  width: 450px;
  padding: 10px 20px;
  border-radius: 25px;
  border: none;
  background-color: var(--searchbar-color);
  color: var(--primary-text);
  font-family: 'Inter', sans-serif;
}

.auth-buttons {
  display: flex;
  gap: 20px;
  align-items: center;
  margin-right: 30px;
}

.signup-btn,
.login-btn {
  padding: 10px 20px;
  border: none;
  background: transparent;
  color: var(--primary-text);
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  cursor: pointer;
}
</style> 