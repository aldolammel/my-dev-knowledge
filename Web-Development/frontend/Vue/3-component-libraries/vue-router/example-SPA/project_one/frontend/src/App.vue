<!--
  FILE: /frontend/src/App.vue
-->
<script setup>
import NavMain from './components/NavMain.vue'
</script>

<template>
  <NavMain />
  <!-- Area where route views (called by RouterLink's in <NavMain />) will be rendered: -->
  <RouterView />
</template>