<script setup>
import { computed } from 'vue';

// Let's bring the fake book database to be accessed by this component too:
// It's a good practice to type the props variable!
let { books } = defineProps({
  books: {
    type: Array,
    required: true,
  }
});

// Computed properties:
let booksRead = computed(() => {
  return books.filter(book => book.isRead).length;
});
/* let percentualRead = computed(() => {
  if (books.length === 0) return 0;
  return (booksRead.value / books.length) * 100;  // To round the result, use Math.round(<code>)
}); */
</script>

<template>
  <div
    class="books-read"
  >
    <label
      for="progress"
    >
      Your progress
    </label><br>
    <progress
      :value="booksRead"
      :max="books.length"
    />
    <p>{{ `${booksRead} of ${books.length} books read` }}</p>
  </div>
</template>

<style>
</style>