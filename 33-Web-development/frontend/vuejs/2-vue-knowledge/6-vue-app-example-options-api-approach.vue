<!-- 
  
  Using the "Options API" approach:
  More about: /33-Web-development/frontend/vuejs/2-vue-knowledge/4-component-approach.txt 

-->

<script>
// Importing things:
// Reserved space...

export default {
  // Component state/data
  data() {
      return {
      count: 0,
      user: null
      }
  },

  // Lifecycle hooks
  // /33-Web-development/frontend/javascript/lifecycle-hooks.js
  mounted() {
      console.log('Component is mounted!')
  },

  // Methods/functions
  methods: {
      increment() {
      this.count++
      }
  },

  // Computed properties
  computed: {
      doubleCount() {
          return this.count * 2
      }
  }
}
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