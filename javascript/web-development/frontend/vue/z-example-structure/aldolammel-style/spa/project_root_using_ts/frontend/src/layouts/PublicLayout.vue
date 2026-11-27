<script setup lang="ts">
import MainMenu from "@/components/navigation/MainMenu.vue";
import FooterMenu from "@/components/navigation/FooterMenu.vue";
</script>

<template>
  <MainMenu />

    <!-- /views/public/*.vue load here: -->
    <RouterView />

  <FooterMenu />
</template>
