<!-- Parent Component (App.vue) -->
<script setup>
  import { ref, provide } from 'vue'
  import ChildComponent from './components/ChildComponent.vue'

  // Reactive state
  const counter = ref(0)

  // Functions to be injected
  const increment = () => {
    counter.value++
  }

  const decrement = () => {
    counter.value--
  }

  const reset = () => {
    counter.value = 0
  }

  // Provide functions to child components
  // Using provide() to make functions available for injection
  provide('counterFunctions', {
    increment,
    decrement,
    reset
  })

  // Also provide the counter value itself
  provide('counterValue', counter)
</script>

<template>
  <div>
    <h1>Parent Component</h1>
    <p>Counter: {{ counter }}</p>
    <button @click="increment">
      Increment from Parent
    </button>
    <button @click="decrement">
      Decrement from Parent
    </button>
    
    <!-- Child component will inject the functions -->
    <ChildComponent />
  </div>
</template>