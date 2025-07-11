<template>
  <!-- This <Person /> is the 'childComponent.vue' file -->
  <!-- This 'contacts' is what your child-components are waiting for: -->
  <!-- This 'toggle-fav' is the name of the emit ('function') that comes back from child component: -->
  <Person
    :contacts="fakeDatabase"
    @toggle-fav="toggleFav"
  />
  <!-- This <AddPerson /> is the 'AnotherChildComponent.vue' file -->
  <!-- This 'add-person' is the name of the emit ('function') that comes back from another child component: -->
  <AddPerson
    @add-person="addPerson"
  />
</template>

<script>
  import Person from './components/ChildComponent.vue'
  import AddPerson from './components/AnotherChildComponent.vue'

  export default {
    name: 'ParentComponent',

    // Register child component
    components: {
      Person,
      AddPerson
    },

    // In Options-API, everything in data() doesn't need to use ref() or reactive() coz they are
    // automatically applied:
    data() {
      return {
        // Fake database:
        fakeDatabase: [
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
        ]
      }
    },
    
    // Event handler methods
    methods: {
      // It was created because in the child component is possible the user update a data (from parent):
      toggleFav(contactId) {
        const contact = this.fakeDatabase.find(c => c.id === contactId)
        if (contact) {
          contact.isFav = !contact.isFav
        }
      },
      // If a child-component asks the parent component to update the contact database, it will be ran:
      addPerson(name, country) {
        // Creating an obj with the new data:
        const newPerson = {
          id: (this.fakeDatabase.length) + 1,
          name: name,
          country: country,
          isFav: false,
        }
        // Adding the new data to the database:
        this.fakeDatabase.push(newPerson)
      }
    }
  }
</script>