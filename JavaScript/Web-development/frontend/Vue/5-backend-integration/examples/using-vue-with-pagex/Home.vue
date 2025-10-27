<script setup>
// THIS FILE: /project_django/frontend/src/components/pages/Home.vue

import { computed, onMounted, watch } from "vue";
import { useRoute } from "vue-router"; // Vue Router
import { usePagesStore } from "@/stores/pages"; // Vue Pinia
// Layout components:
// Reserved Space...
// Common components:
import HeroBig from "@/components/common/HeroBig.vue";

const route = useRoute();
const store = usePagesStore();

// Determine which page slug to use:
const slug = computed(() => {
  // if route has slug param, use it (e.g., /about):
  if (route.params.slug) return route.params.slug;
  // otherwise, find the is_home page:
  const homePage = Object.values(store.pages).find((p) => p.is_home);
  return homePage ? homePage.slug : null;
});

// Get the actual page data object from store:
const pg = computed(() => {
  return slug.value ? store.pages[slug.value] : null;
});

// Fetch page data when component mounts or slug changes:
onMounted(async () => {
  if (slug.value) {
    await store.fetchPage(slug.value);
  }
});
watch(slug, async (newSlug) => {
  if (newSlug) {
    await store.fetchPage(newSlug);
  }
});
</script>

<template>
  <HeroBig
    :title="pg.content['7990_titulo'].v"
    :subtitle="pg.content['915_subtitulo'].v"
    bt-text="Saiba mais"
    :bt-link="pg.content['3651_hyperlink'].v"
    :img="pg.content['7022_imagem'].v"
  />
  <p>...</p>
</template>

<style lang="scss" scoped></style>
