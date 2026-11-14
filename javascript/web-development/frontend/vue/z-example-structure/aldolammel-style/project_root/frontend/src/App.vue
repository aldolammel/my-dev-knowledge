<script setup>
import { useHead } from "@unhead/vue";
// Layout components:
import AppHeader from "@/components/layout/AppHeader.vue";
import AppFooter from "@/components/layout/AppFooter.vue";
// Common components:
// Reserved space...
useHead({
  meta: [
    {
      name: "author",
      content: "@aldolammel",
    },
    // Other meta declarations like description and keywords are in each page component.
  ],
});
</script>

<template>
  <AppHeader />

  <!-- Where router loads each route defined in its RouterLink's: -->
  <RouterView />

  <AppFooter />
</template>

<style lang="scss" scoped></style>
