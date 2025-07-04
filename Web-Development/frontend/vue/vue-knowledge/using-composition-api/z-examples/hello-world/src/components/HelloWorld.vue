<script setup>  // This 'setup' indicates Vue's waiting for 'Composition API' approach.
  // Creating a one-way-data-flow to this this file (child-component) from
  // its parent-component (App.vue):
  defineProps({
    title: {
      type: String,
      required: true,  // mandatory data!
      validator: function(value) {
        // If title is not empty, Vue won't print out a warning in its browser console:
        return value !== '';
      }
    },
    subtitle: {
      type: String,
    },
  })
</script>

<template>
  <!-- All this data below's coming from parent-component (App.vue) via declared Props above -->
  <h1>{{ title }}</h1>
  <p>{{ subtitle }}</p>
</template>

<style scoped>
  /* Nothing to show here because I'm using a external .css file */
</style>
