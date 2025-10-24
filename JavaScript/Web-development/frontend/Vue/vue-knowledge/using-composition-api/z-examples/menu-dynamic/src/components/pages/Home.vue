<script setup>
import { computed, onMounted, watch } from "vue";
import { useRoute } from "vue-router"; // Vue Router
import { usePagesStore } from "@/stores/pages"; // Vue Pinia
// Layout components:
//...
// Common components:
//...

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
 <!-- ... -->>
</template>

<style lang="scss" scoped></style>
