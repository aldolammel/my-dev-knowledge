<script setup>
import Child from './components/ChildComponent.vue'
import { provide } from 'vue'

// Providing data to this parent's descendants without Props feature:
provide('message', 'hello!')
</script>

<template>
  <!-- This <Child /> is the 'ChildComponent.vue' file -->
  <Child />
</template>