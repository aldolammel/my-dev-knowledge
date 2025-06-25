<!-- 
  
  Using the "Composition API" approach:
  More about: /33-Web-development/frontend/vue/vue-knowledge/using-composition-api/

-->


<!--
	
	Vue app starts when index.html calls the Vue init file:
		/Web-Development/frontend/vue/vue-knowledge/3-example-main-html.html

	Vue init file:
		/Web-Development/frontend/vue/vue-knowledge/3-example-vue-init.js

-->

<script setup>
	// By convention, in Composition API approach, script layer should be the first layer!
	import { ref } from 'vue'

	// Reactive data using ref()
	const message = ref('Hello World')

	// Function (equivalent to methods in Options API)
	const updateMessage = () => {
		message.value = 'Updated!'
	}
</script>

<template>
</template>

<style>
</style>