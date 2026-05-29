<script setup>
// THIS FILE: /project_django/frontend/src/components/layout/NavFooter.vue

import { onMounted, computed } from "vue";
import { RouterLink, useRoute } from "vue-router"; // Vue Router
import { useMenusStore } from "@/stores/menus"; // Vue Pinia

// Receiving Props from Parent:
const props = defineProps({
  // menuKey (menu-key) is a "key_of_a_menu" defined on CMS:
  menuKey: {
    type: String,
    required: true,
  },
});
// Declarations:
const route = useRoute();
const store = useMenusStore();
// Fetch menu on component mount:
onMounted(async () => {
  if (!store.menus[props.menuKey]) {
    await store.fetchMenu(props.menuKey);
  }
});
// Computed property to get links from store:
const links = computed(() => store.menus[props.menuKey] || []);
// Check if current route matches link URL:
const isActive = (url) => route.path === url || route.path.startsWith(`${url}/`);
</script>

<template>
  <div class="col-lg-8">
    <!-- Start Footer/Navigation -->
    <div class="row links-wrap">
      <div class="col-6 col-sm-6 col-md-3">
        <ul class="list-unstyled">
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
    <!-- End Footer/Navigation -->
  </div>
</template>

<style lang="scss" scoped></style>
