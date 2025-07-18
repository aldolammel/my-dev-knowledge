<!-- Child Component (ChildComponent.vue) -->
<template>
  <div>
    <h2>Child Component</h2>
    <p>Injected Counter: {{ injectedCounter() }}</p>
    
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

<script>
export default {
  name: 'ChildComponent',
  
  // Inject the functions and data from parent
  inject: ['counterFunctions', 'counterValue'],
  
  // Create computed properties or methods to use injected values
  computed: {
    // Access injected functions
    functions() {
      return this.counterFunctions
    },
    
    // Access injected counter value
    injectedCounter() {
      return this.counterValue
    }
  },
  
  // Alternative: You can also use injected functions directly in methods
  methods: {
    // Example of using injected functions in component methods
    handleCustomAction() {
      this.counterFunctions.increment()
      // Additional logic can be added here
    }
  }
}
</script>