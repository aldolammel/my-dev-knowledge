<script setup>
import { ref, reactive } from 'vue';
import Books from './components/Books.vue';
import BookProgress from './components/BookProgress.vue';
import AddBook from './components/AddBook.vue';

// Fake book database for this example:
let dbBooks = reactive([
  {
    id: 1,
    title: "History of Europe",
    cover:
      "https://m.media-amazon.com/images/I/91qESL6n5sL._SL1500_.jpg",
    isRead: true,
    isbn: "0-235-88844-6",
    author: "Daniel Trejo",
  },
  {
    id: 2,
    title: "Penguin Classics",
    cover:
      "https://m.media-amazon.com/images/I/91cKrZxBuwL.jpg",
    isRead: false,
    isbn: "0-395-07157-8",
    author: "Daniel Trejo, Jon Snow",
  },
  {
    id: 3,
    title: "Becoming",
    cover:
      "https://m.media-amazon.com/images/I/81cJTmFpG-L._UF1000,1000_QL80_.jpg",
    isRead: false,
    isbn: "1-235-74341-4",
    author: "Daniel Trejo",
  },
  {
    id: 4,
    title: "Dia 922, Uma Longa História Sobre Estrada",
    cover:
      "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1640401550i/59926051.jpg",
    isRead: false,
    isbn: "0-572-26222-7",
    author: "Aldo Lammel",
  },
]);

function addBook(newBook) {
  // It receives the newBook (obj sent by the emit in a child component [AddBook.vue] to its
  // parent component [App.vue]).
  // Add the obj into the fake db:
  dbBooks.push(newBook);
  // Close the AddBook window:
  showAddBook.value = false;
}

let showAddBook = ref(false);

function toggleIsRead(id) {
  // This function changes the book read status if its button is clicked.
  const book = dbBooks.find(book => book.id === id);
  if (book) {
    book.isRead = !book.isRead;
  }
};

</script>

<template>
  <div
    v-if="!showAddBook"
    class="container"
  >
    <h1>Meus Livros</h1>
    <div class="header-btns">
      <button
        class="btn"
        @click="showAddBook = true"
      >
        Adicionar Livro +
      </button>
    </div>

    <div class="books-container">
      <!-- Defining which props to use: -->
      <Books
        :books="dbBooks"
        @toggle-is-read="toggleIsRead"
      />
      <BookProgress :books="dbBooks" />
    </div>
  </div>
  <div
    v-else
    class="container"
  >
    <AddBook 
      @add-book="addBook"
      @close-add-book="showAddBook = false"
    />
  </div>
</template>

<style lang="scss">

</style>