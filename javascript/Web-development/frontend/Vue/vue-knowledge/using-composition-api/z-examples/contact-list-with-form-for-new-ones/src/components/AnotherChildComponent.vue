<script setup>
import { ref } from 'vue'

// Storing the inputs data (v-model in those inputs will populate these vars):
// They can be called as 'reactive references' once they are using ref() to work properly
// with v-model.
const inputValueName = ref('')
const inputValueCountry = ref('')

// Emits, declaring:
const emit = defineEmits(['add-person'])

// Function that will emit an event if the form's sent:
const submitForm = () => {
  // Check the data before:
  if (!inputValueName.value || !inputValueCountry.value) {
    alert('All fields are mandatory!')
    // Stop the entire function:
    return false
  }
  // Emitting event change to the parent:
  emit('add-person', inputValueName.value, inputValueCountry.value)
  // Fields' cleaner:
  inputValueName.value = ''
  inputValueCountry.value = ''
  // Debug purposes:
  console.log('A new person was added!')
}
</script>

<template>
  <!-- If submitted, the form emits a custom event to parent, telling it something changed: -->
  <form
    class="spacer"
    @submit.prevent="submitForm"
  >
    <!--
      The v-model directive automatically updates the respective ref() variables.
      So inputValueName.value and inputValueCountry.value will contain the current input values.
      Any changes to these refs will also update the input field values automatically.
    -->
    <div>
      <label>
        New person
        <input
          v-model="inputValueName"
          type="text"
          placeholder="First name"
        >
      </label>
    </div>
    <div>
      <label>
        Country
        <input
          v-model="inputValueCountry"
          type="text"
          placeholder="Their country"
        >
      </label>
    </div>
    <button type="submit">
      Add this person
    </button>
  </form>
</template>