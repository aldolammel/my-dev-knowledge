<script setup>  // This 'setup' indicates Vue's waiting for 'Composition API' approach.
// Importing a child component:
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <!-- Content of the Parent component (main-app) -->
  <p>Welcome:</p>
  <!-- Child component (sub-app)-->
  <HelloWorld
    title="Hello, world!"
    subtitle="I'm using Vue LOCAL installation."
  />
</template>

<style scoped>
  /* Nothing to show here because I'm using a external .css file */
</style>
