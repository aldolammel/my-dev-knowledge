<!-- Parent Component (App.vue) -->
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

<script>
  import ChildComponent from './components/ChildComponent.vue'

  export default {
    name: 'App',
    components: {
      ChildComponent
    },
    
    // Provide functions and data to child components
    provide() {
      return {
        // Provide functions - they maintain 'this' context
        counterFunctions: {
          increment: this.increment,
          decrement: this.decrement,
          reset: this.reset
        },
        
        // Provide reactive data
        // Note: In Options API, we need to use a function to maintain reactivity
        counterValue: () => this.counter
      }
    },
    
    // Data contains reactive state
    data() {
      return {
        counter: 0
      }
    },
    
    // Methods define the functions to be provided
    methods: {
      increment() {
        this.counter++
      },
      
      decrement() {
        this.counter--
      },
      
      reset() {
        this.counter = 0
      }
    }
  }
</script>