<script setup>
// THIS FILE: /project_django/frontend/src/App.vue

// Layout components:
import AppHeader from "@/components/layout/AppHeader.vue";
import AppFooter from "@/components/layout/AppFooter.vue";
// Common components:
// Reserved space...
</script>

<template>
  <AppHeader />

  <!-- Where router loads each route defined in its RouterLink's: -->
  <RouterView />

  <AppFooter />
</template>

<style lang="scss" scoped></style>
