<template>
  <h1>Contacts</h1>
  <!-- In Options-API, if for-loop is used, the array doesn't demand 'props.' before the array -->
  <div
    v-for="contact in contacts"
    :key="contact.id"
  >
    <hr>
    <h3 :class="{ fav : contact.isFav }">
      <a
        href="#"
        @click.prevent="handleToggleFav(contact.id)"
      >
        <span v-if="contact.isFav">★</span>
        {{ contact.name }}
      </a>
    </h3>
    <p>{{ contact.country }}</p>
  </div>
</template>

<script>
  export default {
    // Props declaration:
    props: {
      contacts: {
        type: Array,
        required: true
      }
    },

    // Emits declaration:
    emits: ['toggle-fav'],

    // In Options-API, everything in data() doesn't need to use ref() or reactive() coz they are
    // automatically applied:
    data() {
      return {}
    },

    // Methods
    methods: {
      // Emits function:
      handleToggleFav(contactId) {
        this.$emit('toggle-fav', contactId)
      }
    }
  }
</script>