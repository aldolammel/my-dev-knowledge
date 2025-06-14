<script setup>

import {computed} from 'vue';

// It's a good practice to type the variable:
const { courses } = defineProps({
  courses: {
    type: Array,
    required: true,
  }
});

const coursesDone = computed(() => {
  return courses.filter(course => course.isDone);
})
</script>

<template>
  <div>
    {{ `${coursesDone.length} completed courses of ${courses.length} listed.` }}
  </div>
</template>

<style lang="scss">
</style>