import './assets/base.css'
import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import axios from 'axios'

// 导入字体
import '@fontsource/alumni-sans'
import '@fontsource/anta'
import '@fontsource/inter'

// API Service
const API = {
    BASE_URL: 'http://localhost:8000/api',
    IMAGE_BASE_URL: 'http://localhost:8000/',

    async getCategories() {
        console.log('Attempting to fetch categories from:', `${this.BASE_URL}/categories`);
        try {
            const response = await axios.get(`${this.BASE_URL}/categories`);
            if (!response.ok) throw new Error('Failed to fetch categories');
            console.log('Categories fetched successfully:', response.data);
            return response.data;
        } catch (error) {
            console.error('Error fetching categories:', error);
            throw error;
        }
    },

    async getArticles(filter = 'all', page = 1, categoryId = null) {
        console.log('Attempting to fetch articles with params:', { filter, page, categoryId });
        try {
            const params = new URLSearchParams({
                filter,
                page: page.toString(),
                ...(categoryId && { category_id: categoryId.toString() })
            });
            console.log('Making request to:', `${this.BASE_URL}/articles?${params}`);

            const response = await axios.get(`${this.BASE_URL}/articles?${params}`);
            if (!response.ok) throw new Error('Failed to fetch articles');
            console.log('Articles fetched successfully:', response.data);
            return response.data;
        } catch (error) {
            console.error('Error fetching articles:', error);
            throw error;
        }
    }
};

// 创建 Vue 应用实例
const app = createApp(App)

// 全局注入 API 服务
app.config.globalProperties.$api = API

app.use(createPinia())

app.mount('#app') 