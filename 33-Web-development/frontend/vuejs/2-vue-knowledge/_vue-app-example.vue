<template>
    <div>
      <h1>
        Template tag here shouldn't be empty in any case.
      </h1>
    </div>
  </template>
  
  <script>
  // import HelloWorld from './components/HelloWorld.vue'
  
  export default {
    name: 'App',
    components: {
      // HelloWorld
    }
  }
  </script>
  
  <style lang="scss">
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
  