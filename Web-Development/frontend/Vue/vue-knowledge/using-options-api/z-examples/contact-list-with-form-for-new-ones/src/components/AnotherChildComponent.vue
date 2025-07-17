<template>
  <!-- If submitted, the form emits a custom event to parent, telling it something changed: -->
  <form
    class="spacer"
    @submit.prevent="submitForm"
  >
    <!--
      The v-model directive automatically updates inputValueName and inputValueCountry.
      So they will contain the current input values. Any changes to these refs will also update
      the input field values automatically.
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

<script>
  export default {
    // Props declaration:
    // Reserved space...

    // Emits declaration:
    emits: ['add-person'],

    // In Options-API, everything in data() doesn't need to use ref() or reactive() coz they are
    // automatically applied:
    data() {
      return {
        // Storing the inputs data (v-model in those inputs will populate these vars):
        // They can be called as 'reactive references' once they are using ref() to work properly
        // with v-model.
        inputValueName: '',
        inputValueCountry: ''
      }
    },

    methods: {
      // Emits function:
      // Function that will emit an event if the form's sent.
      submitForm() {
        // Check the data before:
        if (!this.inputValueName || !this.inputValueCountry) {
          alert('All fields are mandatory!')
          // Stop the entire function:
          return false
        }
        // Emitting event change to the parent:
        this.$emit('add-person', this.inputValueName, this.inputValueCountry)
        // Fields' cleaner:
        this.inputValueName = ''
        this.inputValueCountry = ''
        // Debug purposes:
        console.log('A new person was added!')
      }
    }
  }
</script>