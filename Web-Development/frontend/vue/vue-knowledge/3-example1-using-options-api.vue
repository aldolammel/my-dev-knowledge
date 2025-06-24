<!-- 
  
  Using the "Options API" approach:
  More about: /33-Web-development/frontend/vue/vue-knowledge/using-options-api/

-->

<template>
</template>

<script>
export default {
  // Component name (optional but recommended)
  name: 'MyComponent',
  
  // Reactive data properties
  data() {
    return {
      message: 'Hello World'
    }
  },
  
  // Component methods
  methods: {
    updateMessage() {
      this.message = 'Updated!'
    }
  }
}
</script>

<style>
</style>