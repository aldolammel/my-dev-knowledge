<template>
  <div id="nav">
    <router-link to="/">
      Home
    </router-link> -
    <router-link to="/product">
      Product
    </router-link> -
    <router-link to="/cart">
      Cart ({{ cart.length }})
    </router-link>
  </div>
  <router-view />
</template>

<script>
  // Things to import:
  import { mapState } from 'vuex'

  export default {
    
    // Computed properties:
    // /JavaScript/Web-development/frontend/Vue/3-component-libraries/vuex/computed-properties.txt
    // /JavaScript/Web-development/frontend/Vue/3-component-libraries/vuex/vuex-helpers.txt
    computed: mapState([
      'cart'  // It's a state property (data)!
    ]),

    // Lifecycle hook:
    created() {
      // It calls the action to load the products:
      this.$store.dispatch('actLoadProducts');

      // It calls the action to load all products in shopping cart (empty or not):
      // A shopping cart using this approach avoid data-lost if user open the cart in a
      // new browser tab/window.
      this.$store.dispatch('actLoadCart');
      
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
    max-width: 1280px;
    margin: 80px auto;
  }

  #nav {
    padding: 16px 0;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    width: 100%;
    text-align: center;
    background-color: rgb(37, 37, 37);
    color: white;


    a {
      color: white;
      text-decoration: none;

      &.router-link-exact-active {
        color: #007bff;
      }
    }
  }
</style>
