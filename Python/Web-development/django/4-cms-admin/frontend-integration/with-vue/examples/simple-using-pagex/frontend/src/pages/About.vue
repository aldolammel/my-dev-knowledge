<!--
  FILE: /my_django_project/frontend/src/pages/About.vue
-->
<script setup>
import { onMounted } from 'vue'
import { usePagesStore } from '../stores/pages'
import { pagesConstants } from './pagesConstants'
//...

const pagesStore = usePagesStore()
const pageId = pagesConstants.PID_B  // Use Page ID because it barely change.

onMounted(async () => {
  await pagesStore.fetchPage(pageId)
})

//...
</script>

<template>
  <!-- Start Hero Section -->
  <div v-if="pagesStore.pages[pageId]">
    <div>
      <h1>{{ pagesStore.pages[pageId].seo_title }}</h1>
      <p>{{ pagesStore.pages[pageId].seo_desc }}</p>
    </div>  
    <div v-if="pagesStore.pages[pageId].img_highlight">
      <img :src="pagesStore.pages[pageId].img_highlight">
    </div>
  </div>
  <!-- End Hero Section -->
  <!-- ... -->
</template>