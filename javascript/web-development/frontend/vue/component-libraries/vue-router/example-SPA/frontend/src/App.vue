<!--
  FILE: /frontend/src/App.vue
-->
<script setup lang="ts">
// Components:
import MainMenu from "@/components/navigation/MainMenu.vue";
import FooterMenu from "@/components/navigation/FooterMenu.vue";

// Custom HTML <head>:
// Reserved space...
</script>

<template>

  <MainMenu />
  
  <!-- Where router loads each route defined in its RouterLink's: -->
  <RouterView />

  <FooterMenu />

</template>

<style lang="scss" scoped></style>