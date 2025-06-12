<!-- 
  
  Using the "Options API" approach:
  More about: /33-Web-development/frontend/vue/vue-knowledge/using-options-api/

-->

<template>
</template>

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

  // Computed properties
  // /33-Web-development/frontend/vue/computed-properties.txt
  computed: {
      doubleCount() {
          return this.count * 2
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
  }
}
</script>

<style>
</style>