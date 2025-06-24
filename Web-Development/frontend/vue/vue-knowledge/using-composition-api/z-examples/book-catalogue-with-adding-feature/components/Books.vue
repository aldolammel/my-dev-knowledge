<script setup>
  // It's a good practice to define emits, and always before props:
  const emit = defineEmits(['toggleIsRead'])
  // It's a good practice to type the variable:
  let { books } = defineProps({
    books: {
      type: Array,
      required: true,
    }
  });
</script>

<template>
  <div class="books-list">
    <template v-if="!books.length">
      <p>No books yet.</p>
    </template>
    <template v-else>
      <div
        v-for="book in books"
        :key="book.isbn"
        class="book"
      >
        <div 
          v-if="book.isRead"
          class="readIt"
        >
          <i class="fa-solid fa-eye" />
        </div>
        <div class="book-cover">
          <img 
            :src="book.cover"
            :alt="book.title"
          >
          <button
            :class="{ isRead : book.isRead }"  
            @click="emit('toggleIsRead', book.id)"
          >
            <i class="fa-solid fa-eye" />
            <span>
              {{ book.isRead ? 'Read!' : 'Not read yet' }}
            </span>
          </button>
        </div>
        <div class="book-details">
          <p class="book-author">
            {{ book.author }}
          </p>
          <h3 class="book-title">
            {{ book.title }}
          </h3>
          <p>
            <i class="fa-solid fa-hashtag icon" />
            {{ book.isbn }}
          </p>
        </div>
      </div>
    </template>
  </div>
</template>

<style>
</style>