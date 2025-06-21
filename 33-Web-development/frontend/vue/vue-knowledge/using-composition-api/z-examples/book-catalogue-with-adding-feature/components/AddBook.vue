<script setup>
  const emit = defineEmits(['closeAddBook', 'addBook']);

  let newBook = {
    //id: 0,  // in a real case, let the database handle it. 
    title: "",
    isRead: false,
    isbn: "",
    author: "",
    //cover: "",
  };

</script>

<template>
  <h1>Add Book</h1>
    
  <div class="header-btns">
    <button
      class="btn"
      @click="emit('closeAddBook')"
    >
      Fechar x
    </button>
  </div>
 
  <form class="add-form">
    <div class="form-control">
      <label>Title</label>
      <input
        v-model="newBook.title"
        type="text"
        name="text"
        placeholder="Add the book title"
        required
      >
    </div>
    <div class="form-control">
      <label>Cover</label>
      <input 
        v-model="newBook.cover" 
        type="text" 
        name="cover"
        placeholder="Add the book cover URL"
        required
      >
    </div>
    <div class="form-control">
      <label>Author</label>
      <input
        v-model="newBook.author"
        type="text"
        name="author"
        placeholder="Add an author"
      >
    </div>
    <div class="form-control">
      <label>ISBN#</label>
      <input 
        v-model="newBook.isbn" 
        type="text" 
        name="isbn"
        placeholder="Add the ISBN number"
      >
    </div>
    <div class="form-control form-control-check">
      <input 
        id="readIt" 
        v-model="newBook.isRead" 
        type="checkbox"
        name="readIt"
      >
      <label for="readIt">Already read</label>
    </div>

    <button
      type="submit"
      class="btn btn-block"
      @click.prevent="emit('addBook', newBook)"
    >
      Save book
    </button>
  </form>
</template>

<style>
</style>