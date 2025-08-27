<script setup>
import Child from './components/ChildComponent.vue'
import { ref } from 'vue'

// Fake database:
const fakeDatabase = ref([
  {
    id: 1,
    name: 'Joanna',
    country: 'Brazil',
    isFav: false,
  },
  {
    id: 2,
    name: 'Yoshy',
    country: 'Japan',
    isFav: true,
  },
])
// It was created coz in the child component is possible the user update a data (from parent):
function toggleFav(contactId) {
  const contact = fakeDatabase.value.find(c => c.id === contactId)
  if (contact) {
    contact.isFav = !contact.isFav
  }
}
// If a child-component asks the parent component to update the contact database, it will be ran:
function addPerson(name, country) {
  // Creating an obj with the new data:
  const newPerson = {
    id: (fakeDatabase.value.length) + 1,
    name: name,
    country: country,
    isFav: false,
  }
  // Adding the new data to the database:
  fakeDatabase.value.push(newPerson)
}
</script>

<template>
  <!-- This <Child /> is the 'ChildComponent.vue' file -->
  <!-- This 'contacts' is what your child-components are waiting for: -->
  <!-- This 'toggle-fav' is the name of the emit ('function') that comes back from child component: -->
  <!-- This 'add-person' is the name of the emit ('function') that comes back from another child component: -->
  <Child
    :contacts="fakeDatabase"
    @toggle-fav="toggleFav"
    @add-person="addPerson"
  />
</template>