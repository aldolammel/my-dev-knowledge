<script setup>
// THIS FILE: /project_django/frontend/src/components/layout/NavMain.vue

import { onMounted, computed } from "vue";
import { RouterLink, useRoute } from "vue-router"; // Vue Router
import { useMenusStore } from "@/stores/menus"; // Vue Pinia
// Layout components:
// Reserved Space...
// Common components
// Reserved Space...

// Receiving Props from Parent:
const props = defineProps({
  identifier: {
    type: String,
    required: true,
  },
});
// Declarations:
const route = useRoute();
const store = useMenusStore();
// Fetch menu on component mount:
onMounted(async () => {
  if (!store.menus[props.identifier]) {
    await store.fetchMenu(props.identifier);
  }
});
// Computed property to get links from store:
const links = computed(() => store.menus[props.identifier] || []);
// Check if current route matches link URL:
const isActive = (url) => route.path === url || route.path.startsWith(`${url}/`);
</script>

<template>
  <!-- Start Header/Navigation -->
  <nav
    class="custom-navbar navbar navbar navbar-expand-md navbar-dark bg-dark"
    arial-label="Furni navigation bar"
  >
    <div class="container">
      <RouterLink class="navbar-brand" to="/">IBCPA</RouterLink>

      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarsFurni"
        aria-controls="navbarsFurni"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon" />
      </button>

      <div id="navbarsFurni" class="collapse navbar-collapse">
        <ul class="custom-navbar-nav navbar-nav ms-auto mb-2 mb-md-0">
          <li
            v-for="link in links"
            :key="link.id"
            class="nav-item"
            :class="{ active: isActive(link.url) }"
          >
            <RouterLink v-if="link.link_type !== 'redirection'" :to="link.url" class="nav-link">
              {{ link.title }}
            </RouterLink>
            <a
              v-else
              :href="link.url"
              class="nav-link"
              :target="link.url_target"
              rel="noopener noreferrer"
            >
              {{ link.title }}
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <!-- End Header/Navigation -->
</template>

<style lang="scss" scoped></style>
