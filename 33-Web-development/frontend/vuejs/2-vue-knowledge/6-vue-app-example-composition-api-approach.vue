<script setup>
// Using the "Composition API" approach:
// More about: /33-Web-development/frontend/vuejs/2-vue-knowledge/4-component-approach.txt
import { ref } from 'vue'
// Direct code here
</script>

<template>
  <div>
    <h1>
      Template tag here shouldn't be empty in any case.
    </h1>
  </div>
</template>

<style>
/* 
  In case of the SCSS component is enabled on project,
  use <style lang="scss">
*/
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 60px auto;
  max-width: 960px;
}
</style>