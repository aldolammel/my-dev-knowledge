<script setup>
// Importing the inject method to call something provided by this component parent:
import { inject } from 'vue'

// This injection is coming directly from the Grand-Parent-component (ParentComponent), and
// not from its parent (ChildComponent.vue):
const message = inject('message')
</script>

<template>
  <div>
    {{ message }}
  </div>
</template>