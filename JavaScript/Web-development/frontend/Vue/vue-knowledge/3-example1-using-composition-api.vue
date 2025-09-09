<!-- 
  
  Using the "Composition API" approach:
  More about: /JavaScript/Web-development/frontend/Vue/vue-knowledge/using-composition-api/

-->


<!--
	
	Vue app starts when index.html calls the Vue init file:
		/JavaScript/Web-development/frontend/Vue/vue-knowledge/3-example-main-html.html

	Vue init file:
		/JavaScript/Web-development/frontend/Vue/vue-knowledge/3-example-vue-init.js

-->

<!-- By convention, in Composition API approach, script layer should be the first layer! -->
<script setup>
import { ref } from 'vue'

// Reactive data using ref()
const message = ref('Hello World')

// Methods, unlike in Options API, you can set them anywhere in the .vue's script layer:
const updateMessage = () => {
	message.value = 'Updated!'
}
</script>

<template>
</template>

<style>
</style>