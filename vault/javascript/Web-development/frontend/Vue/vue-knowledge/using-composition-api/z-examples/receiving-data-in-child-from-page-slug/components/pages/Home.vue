<script setup>
import { computed, onMounted, watch } from "vue";
import { useRoute } from "vue-router"; // Vue Router
import { usePagesStore } from "@/stores/pages"; // Vue Pinia
// Layout components:
import SiteHeader from "@/components/layout/SiteHeader.vue";
// Common components:
// ...

const route = useRoute();
const store = usePagesStore();

// Determine which page slug to use:
const slug = computed(() => {
  if (route.params.slug) return route.params.slug;
  const homePage = Object.values(store.pages).find((p) => p.is_home);
  return homePage ? homePage.slug : null;
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
  <!-- CHILD COMPONENT -->
  <SiteHeader v-if="slug" :page="slug" />
</template>

<style lang="scss" scoped></style>
