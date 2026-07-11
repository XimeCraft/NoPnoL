<template>
  <div class="article-detail">
    <!-- Loading State -->
    <div v-if="loading" class="loading">
      <p>Loading article...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="error">
      <p>{{ error }}</p>
      <button @click="$router.push('/')" class="back-btn">Back to Home</button>
    </div>

    <!-- Article Content -->
    <article v-else-if="article" class="article-content">
      <!-- Article Header -->
      <header class="article-header">
        <div class="breadcrumb">
          <router-link to="/">Home</router-link>
          <span class="separator">/</span>
          <span class="current">{{ article.category?.name || 'Article' }}</span>
        </div>

        <h1 class="article-title">{{ article.title }}</h1>

        <!-- Article Meta -->
        <div class="article-meta">
          <div class="author-info">
            <img
              v-if="article.author?.avatar_url"
              :src="getImageUrl(article.author.avatar_url)"
              :alt="article.author.name"
              class="author-avatar"
            >
            <div class="author-details">
              <p class="author-name">{{ article.author?.name }}</p>
              <p class="author-profession">{{ article.author?.profession }}</p>
            </div>
          </div>
          <div class="article-info">
            <time class="publish-date">{{ formatDate(article.publish_date) }}</time>
            <span class="reading-time">{{ readingTime }} min read</span>
          </div>
        </div>

        <!-- Tags -->
        <div v-if="article.tags && article.tags.length > 0" class="article-tags">
          <span
            v-for="(tag, index) in article.tags"
            :key="tag"
            :class="['tag', `tag-${(index % 3) + 1}`]"
          >
            {{ tag }}
          </span>
        </div>
      </header>

      <!-- Hero Image -->
      <div v-if="article.image_url" class="hero-image">
        <img :src="getImageUrl(article.image_url)" :alt="article.title">
      </div>

      <!-- Article Body -->
      <div class="article-body">
        <div class="content-wrapper">
          <!-- Main Content -->
          <div class="main-content">
            <div class="article-text" v-html="formattedContent"></div>
          </div>

          <!-- Social Sharing Sidebar -->
          <aside class="social-sidebar">
            <div class="social-sticky">
              <h3>Share</h3>
              <div class="social-buttons">
                <button @click="shareOnTwitter" class="social-btn twitter" title="Share on Twitter">
                  <svg viewBox="0 0 24 24" width="20" height="20">
                    <path fill="currentColor" d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                  </svg>
                </button>
                <button @click="shareOnLinkedIn" class="social-btn linkedin" title="Share on LinkedIn">
                  <svg viewBox="0 0 24 24" width="20" height="20">
                    <path fill="currentColor" d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                  </svg>
                </button>
                <button @click="shareOnFacebook" class="social-btn facebook" title="Share on Facebook">
                  <svg viewBox="0 0 24 24" width="20" height="20">
                    <path fill="currentColor" d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                  </svg>
                </button>
                <button @click="copyLink" class="social-btn copy" title="Copy link">
                  <svg viewBox="0 0 24 24" width="20" height="20">
                    <path fill="currentColor" d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/>
                  </svg>
                </button>
              </div>
              <p v-if="linkCopied" class="copy-feedback">Link copied!</p>
            </div>
          </aside>
        </div>
      </div>

      <!-- Related Articles -->
      <section v-if="relatedArticles.length > 0" class="related-articles">
        <h2>Related Articles</h2>
        <div class="related-grid">
          <router-link
            v-for="related in relatedArticles"
            :key="related.id"
            :to="`/article/${related.id}`"
            class="related-card"
          >
            <div class="related-image">
              <img :src="getImageUrl(related.image_url)" :alt="related.title">
            </div>
            <div class="related-content">
              <time class="related-date">{{ formatDate(related.publish_date) }}</time>
              <h3 class="related-title">{{ related.title }}</h3>
              <p class="related-author">{{ related.author?.name }}</p>
            </div>
          </router-link>
        </div>
      </section>
    </article>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()

const API_BASE_URL = 'http://localhost:8000'

const article = ref(null)
const relatedArticles = ref([])
const loading = ref(true)
const error = ref(null)
const linkCopied = ref(false)

// Calculate reading time based on content length
const readingTime = computed(() => {
  if (!article.value?.content) return 0
  const wordsPerMinute = 200
  const wordCount = article.value.content.split(/\s+/).length
  return Math.ceil(wordCount / wordsPerMinute)
})

// Format content with proper HTML structure
const formattedContent = computed(() => {
  if (!article.value?.content) return ''

  // Split content by double newlines to create paragraphs
  const paragraphs = article.value.content
    .split('\n\n')
    .filter(p => p.trim())
    .map(p => `<p>${p.trim()}</p>`)
    .join('')

  return paragraphs
})

// Fetch article data
const fetchArticle = async (id) => {
  try {
    loading.value = true
    error.value = null

    const response = await axios.get(`${API_BASE_URL}/api/articles/${id}`)
    article.value = response.data

    // Fetch related articles (same category)
    if (article.value.category_id) {
      await fetchRelatedArticles(article.value.category_id, id)
    }
  } catch (err) {
    console.error('Error fetching article:', err)
    error.value = 'Failed to load article. Please try again later.'
  } finally {
    loading.value = false
  }
}

// Fetch related articles from the same category
const fetchRelatedArticles = async (categoryId, currentArticleId) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/api/articles`, {
      params: {
        category_id: categoryId,
        limit: 4
      }
    })
    // Filter out current article and limit to 3
    relatedArticles.value = response.data
      .filter(a => a.id !== currentArticleId)
      .slice(0, 3)
  } catch (err) {
    console.error('Error fetching related articles:', err)
  }
}

// Helper functions
const getImageUrl = (path) => {
  if (!path) return ''
  return `${API_BASE_URL}${path.startsWith('/') ? path : '/' + path}`
}

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

// Social sharing functions
const shareOnTwitter = () => {
  const text = encodeURIComponent(article.value.title)
  const url = encodeURIComponent(window.location.href)
  window.open(`https://twitter.com/intent/tweet?text=${text}&url=${url}`, '_blank')
}

const shareOnLinkedIn = () => {
  const url = encodeURIComponent(window.location.href)
  window.open(`https://www.linkedin.com/sharing/share-offsite/?url=${url}`, '_blank')
}

const shareOnFacebook = () => {
  const url = encodeURIComponent(window.location.href)
  window.open(`https://www.facebook.com/sharer/sharer.php?u=${url}`, '_blank')
}

const copyLink = async () => {
  try {
    await navigator.clipboard.writeText(window.location.href)
    linkCopied.value = true
    setTimeout(() => {
      linkCopied.value = false
    }, 2000)
  } catch (err) {
    console.error('Failed to copy link:', err)
  }
}

// Watch for route changes (when navigating between articles)
watch(() => route.params.id, (newId) => {
  if (newId) {
    fetchArticle(newId)
    // Scroll to top when article changes
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
})

onMounted(() => {
  const articleId = route.params.id
  if (articleId) {
    fetchArticle(articleId)
  }
})
</script>

<style scoped>
.article-detail {
  min-height: 100vh;
  background-color: var(--bg-color);
  color: var(--primary-text);
}

/* Loading & Error States */
.loading, .error {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 60vh;
  padding: 40px 20px;
}

.error {
  text-align: center;
}

.back-btn {
  margin-top: 20px;
  padding: 12px 30px;
  background: var(--highlight-color);
  color: var(--bg-color);
  border: none;
  border-radius: 5px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: opacity 0.3s;
}

.back-btn:hover {
  opacity: 0.8;
}

/* Article Content */
.article-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 40px 20px 80px;
}

/* Article Header */
.article-header {
  max-width: 900px;
  margin: 0 auto 40px;
}

.breadcrumb {
  font-size: 14px;
  margin-bottom: 30px;
  color: #999;
}

.breadcrumb a {
  color: var(--highlight-color);
  text-decoration: none;
  transition: opacity 0.3s;
}

.breadcrumb a:hover {
  opacity: 0.7;
}

.separator {
  margin: 0 10px;
}

.current {
  color: #666;
}

.article-title {
  font-family: 'Anta', sans-serif;
  font-size: 48px;
  line-height: 1.2;
  margin: 0 0 30px 0;
  font-weight: 700;
}

.article-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.author-info {
  display: flex;
  align-items: center;
  gap: 15px;
}

.author-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  object-fit: cover;
}

.author-details {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.author-name {
  font-weight: 600;
  font-size: 16px;
  margin: 0;
}

.author-profession {
  font-size: 14px;
  color: #999;
  margin: 0;
}

.article-info {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 4px;
}

.publish-date {
  font-size: 14px;
  color: #999;
}

.reading-time {
  font-size: 14px;
  color: var(--highlight-color);
  font-weight: 500;
}

.article-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 20px;
}

.tag {
  padding: 6px 16px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 500;
}

.tag-1 { background: var(--tag-color-1); }
.tag-2 { background: var(--tag-color-2); }
.tag-3 { background: var(--tag-color-3); }

/* Hero Image */
.hero-image {
  max-width: 1200px;
  margin: 0 auto 60px;
  border-radius: 12px;
  overflow: hidden;
}

.hero-image img {
  width: 100%;
  height: auto;
  display: block;
  aspect-ratio: 2/1;
  object-fit: cover;
}

/* Article Body */
.article-body {
  max-width: 1200px;
  margin: 0 auto;
}

.content-wrapper {
  display: grid;
  grid-template-columns: 1fr 80px;
  gap: 60px;
  align-items: start;
}

.main-content {
  max-width: 800px;
}

.article-text {
  font-family: 'Inter', sans-serif;
  font-size: 18px;
  line-height: 1.8;
  color: #e0e0e0;
}

.article-text :deep(p) {
  margin: 0 0 24px 0;
}

.article-text :deep(p:last-child) {
  margin-bottom: 0;
}

.article-text :deep(h2) {
  font-family: 'Anta', sans-serif;
  font-size: 32px;
  margin: 50px 0 20px 0;
  font-weight: 600;
}

.article-text :deep(h3) {
  font-family: 'Anta', sans-serif;
  font-size: 24px;
  margin: 40px 0 16px 0;
  font-weight: 600;
}

.article-text :deep(ul), .article-text :deep(ol) {
  margin: 20px 0;
  padding-left: 30px;
}

.article-text :deep(li) {
  margin-bottom: 12px;
}

.article-text :deep(a) {
  color: var(--highlight-color);
  text-decoration: none;
  border-bottom: 1px solid var(--highlight-color);
  transition: opacity 0.3s;
}

.article-text :deep(a:hover) {
  opacity: 0.7;
}

/* Social Sidebar */
.social-sidebar {
  position: relative;
}

.social-sticky {
  position: sticky;
  top: 100px;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.social-sticky h3 {
  font-size: 14px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0 0 10px 0;
  color: #999;
}

.social-buttons {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.social-btn {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--searchbar-color);
  border: none;
  border-radius: 50%;
  cursor: pointer;
  transition: all 0.3s;
  color: var(--primary-text);
}

.social-btn:hover {
  transform: scale(1.1);
  background: var(--highlight-color);
}

.social-btn.twitter:hover {
  background: #1DA1F2;
}

.social-btn.linkedin:hover {
  background: #0077B5;
}

.social-btn.facebook:hover {
  background: #1877F2;
}

.copy-feedback {
  font-size: 12px;
  color: var(--highlight-color);
  margin: 5px 0 0 0;
  animation: fadeIn 0.3s;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Related Articles */
.related-articles {
  max-width: 1200px;
  margin: 80px auto 0;
  padding-top: 60px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.related-articles h2 {
  font-family: 'Anta', sans-serif;
  font-size: 36px;
  margin: 0 0 40px 0;
  font-weight: 600;
}

.related-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
}

.related-card {
  display: flex;
  flex-direction: column;
  background: var(--searchbar-color);
  border-radius: 12px;
  overflow: hidden;
  text-decoration: none;
  color: var(--primary-text);
  transition: transform 0.3s, box-shadow 0.3s;
}

.related-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
}

.related-image {
  width: 100%;
  aspect-ratio: 16/9;
  overflow: hidden;
}

.related-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s;
}

.related-card:hover .related-image img {
  transform: scale(1.05);
}

.related-content {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.related-date {
  font-size: 14px;
  color: #999;
}

.related-title {
  font-family: 'Anta', sans-serif;
  font-size: 18px;
  margin: 0;
  font-weight: 600;
  line-height: 1.4;
}

.related-author {
  font-size: 14px;
  color: #999;
  margin: 0;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .content-wrapper {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .social-sidebar {
    order: -1;
  }

  .social-sticky {
    position: static;
    flex-direction: row;
    justify-content: center;
  }

  .social-buttons {
    flex-direction: row;
  }

  .related-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .article-title {
    font-size: 32px;
  }

  .article-meta {
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
  }

  .article-info {
    align-items: flex-start;
  }

  .article-text {
    font-size: 16px;
  }

  .related-grid {
    grid-template-columns: 1fr;
  }

  .related-articles h2 {
    font-size: 28px;
  }
}
</style>
