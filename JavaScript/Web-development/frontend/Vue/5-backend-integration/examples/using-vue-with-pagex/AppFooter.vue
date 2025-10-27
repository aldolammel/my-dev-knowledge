<script setup>
// THIS FILE: /project_django/frontend/src/components/layout/AppFooter.vue

import { onMounted, computed } from "vue";
import { useStructuresStore } from "@/stores/structures"; // Vue Pinia
// Layout components:
import NavFooter from "@/components/layout/NavFooter.vue";
// Common components:
// Reserved space...

const store = useStructuresStore();

// Fetching the content first before to try to display that:
onMounted(async () => {
  await store.fetchStructure("rodape");
});

const struct = computed(() => {
  return store.structures.rodape?.content || {};
});
</script>

<template>
  <!-- Start App Footer Section -->
  <footer class="footer-section">
      <div>
        <p>{{ struct["4891_text_block"]?.v }}</p>
      </div>
      <div>
        <NavFooter identifier="menu_rodape" />
      </div>
      <div>
        {{ new Date().getFullYear() }} © MyCompanyExample | Developed by 
        <a href="https://dev.aldolammel.com" target="_blank"> AL </a>
      </div>
    </div>
  </footer>
  <!-- End App Footer Section -->
</template>

<style lang="scss" scoped></style>
