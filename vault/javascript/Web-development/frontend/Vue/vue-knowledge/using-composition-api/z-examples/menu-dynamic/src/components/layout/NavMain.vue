<script setup>
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

const route = useRoute();
const store = useMenusStore();

onMounted(async () => {
  if (!store.menus[props.menuKey]) {
    await store.fetchMenu(props.menuKey);
  }
});

const links = computed(() => store.menus[props.menuKey] || []);

const isActive = (url) => route.path === url || route.path.startsWith(`${url}/`);
</script>

<template>
  <!-- Start Header/Navigation -->
  <nav
    class="custom-navbar navbar navbar navbar-expand-md navbar-dark bg-dark"
    arial-label="Furni navigation bar"
  >
    <div class="container">
      <RouterLink class="navbar-brand" to="/"> IBCPA </RouterLink>

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

        <ul class="custom-navbar-cta navbar-nav mb-2 mb-md-0 ms-5">
          <li>
            <a class="nav-link" href="#"><img src="@/assets/imgs/user.svg" /></a>
          </li>
          <li>
            <a class="nav-link" href="#"><img src="@/assets/imgs/cart.svg" /></a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <!-- End Header/Navigation -->
</template>

<style lang="scss" scoped></style>
