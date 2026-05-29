<script setup>
import { computed, onMounted, watch } from "vue";
import { useRoute } from "vue-router"; // Vue Router
import { usePagesStore } from "@/stores/pages"; // Vue Pinia
// Layout components:
//...
// Common components:
// ...

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
  <!-- <SiteHeader v-if="slug" :page="slug" /> -->
  <!-- Start Hero Section -->
  <div v-if="pg" class="hero">
    <div class="container">
      <div class="row justify-content-between">
        <div class="col-lg-5">
          <div class="intro-excerpt">
            <h1>
              {{ pg.seo_title }}
            </h1>
            <p class="mb-4">
              {{ pg.content["9065_titulo"]?.v }}
            </p>
            <p>
              <a href="" class="btn btn-secondary me-2">Sabia mais</a
              ><a href="#" class="btn btn-white-outline">Contato</a>
            </p>
          </div>
        </div>
        <div class="col-lg-7">
          <div class="hero-img-wrap">
            <img src="@/assets/imgs/couch.png" class="img-fluid" />
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- End Hero Section -->
  <p>soon...</p>
</template>

<style lang="scss" scoped></style>
