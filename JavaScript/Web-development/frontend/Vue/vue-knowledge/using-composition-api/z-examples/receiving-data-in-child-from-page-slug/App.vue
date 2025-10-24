<script setup>
// Very basic layout components:
import NavMain from "@/components/layout/NavMain.vue";
import SiteFooter from "@/components/layout/SiteFooter.vue";
</script>

<template>
  <!-- Defining Props of menu created through Django CMS Pagex -->
  <NavMain identifier="menu_principal" />

  <!-- Where the router will load each link/route defined in its RouterLink's: -->
  <RouterView />

  <SiteFooter />
</template>

<style lang="scss" scoped></style>
