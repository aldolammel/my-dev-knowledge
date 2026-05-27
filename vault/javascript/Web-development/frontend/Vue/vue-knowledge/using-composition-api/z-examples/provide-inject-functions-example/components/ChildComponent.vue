<!-- Child Component (ChildComponent.vue) -->
<script setup>
import { inject } from 'vue'

// Inject the functions from parent
// inject() retrieves the provided values by key
const functions = inject('counterFunctions')

// Inject the counter value
const injectedCounter = inject('counterValue')

// The injected functions can be used directly in template or other composition functions
// No need to re-declare them, they're already reactive and bound to parent's scope
</script>

<template>
  <div>
    <h2>Child Component</h2>
    <p>Injected Counter: {{ injectedCounter }}</p>
    
    <!-- Using injected functions -->
    <button @click="functions.increment">
      Child Increment
    </button>
    <button @click="functions.decrement">
      Child Decrement
    </button>
    <button @click="functions.reset">
      Child Reset
    </button>
  </div>
</template>