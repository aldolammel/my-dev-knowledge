<script setup>
import NestedChild from './NestedChildComponent.vue'

// Once you need some data from the parent component, the data need to be declared as 'props':
const props = defineProps({
  contacts: {
    type: Array,
    required: true
  }
});

// And once you ask for the parent component update something, it must be declared as 'emit':
const emit = defineEmits(['toggle-fav', 'add-person'])

// Functions that emit requests to update data to their parents:
function handleToggleFav(contactId) {
  emit('toggle-fav', contactId)
}
function addPerson(name, country) {
  emit('add-person', name, country)
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
  <!-- This <NestedChild /> is the 'NestedChildComponent.vue' file -->
  <!-- This 'add-person' is the name of the emit ('function') that comes back from another child component: -->
  <NestedChild
    :contacts="props.contacts"    
    @add-person="addPerson"
  />
</template>