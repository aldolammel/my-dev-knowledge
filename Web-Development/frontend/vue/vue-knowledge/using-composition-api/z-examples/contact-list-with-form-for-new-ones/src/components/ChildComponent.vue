<script setup>
  const props = defineProps({
    contacts: {
      type: Array,
      required: true
    }
  });

  const emit = defineEmits(['toggle-fav'])

  function handleToggleFav(contactId) {
    emit('toggle-fav', contactId)
  }
</script>

<template>
  <h1>Contacts</h1>
  <div
    v-for="contact in props.contacts"
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