<!-- 
  
  Using the "Composition API" approach:
  More about: /33-Web-development/frontend/vue/vue-knowledge/using-composition-api/

-->

<script setup>
import { ref } from 'vue'

// Reactive data using ref()
const message = ref('Hello World')

// Function (equivalent to methods in Options API)
const updateMessage = () => {
  message.value = 'Updated!'
}
</script>

<template>
</template>

<style>
</style>