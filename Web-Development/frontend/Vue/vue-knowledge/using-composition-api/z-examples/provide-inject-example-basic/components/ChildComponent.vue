<script setup>
  // Importing a child of this child component. So in other words, importing a nested child component:
  import NestedChild from './NestedChildComponent.vue'

  // See!? No Props are used to deliver data to this component's children. That said,
  // check now the NestedChildComponent.vue to better understand the Provide/Inject workflow.
</script>

<template>
  <!-- This <NestedChild /> is the 'NestedChildComponent.vue' file -->
  <NestedChild />
</template>