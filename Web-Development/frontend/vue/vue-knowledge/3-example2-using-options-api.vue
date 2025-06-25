<!-- 
  
  Using the "Options API" approach:
  More about: /33-Web-development/frontend/vue/vue-knowledge/using-options-api/

-->


<!--
	
	Vue app starts when index.html calls the Vue init file:
		/Web-Development/frontend/vue/vue-knowledge/3-example-main-html.html

	Vue init file:
		/Web-Development/frontend/vue/vue-knowledge/3-example-vue-init.js

-->

<template>
	<!-- By convention, in Options API approach, template layer should be the first layer -->
</template>

<script>
	// Importing things:
	// Reserved space...

	export default {
		// Component name (optional but recommended)
		//name: 'MyComponent',

		// Component state/data
		data() {
			// 'return' here always need to return an JS obj "{}":
			return {
				// Piece of data that Vue is aware of:
				count: 0,
				user: null
			}
		},

		// Computed properties
		// /Web-Development/frontend/vue/vue-knowledge/using-options-api/_option-computed.vue
		computed: {
			doubleCount() {
				return this.count * 2
			}
		},

		// Lifecycle hooks
		// /JavaScript/Web-development/frontend/lifecycle-hooks.js
		mounted() {
			console.log('Component is mounted!')
		},

		// Methods/functions
		// /Web-Development/frontend/vue/vue-knowledge/using-options-api/_option-methods.vue
		methods: {
			increment() {
				this.count++
			}
		}
	}
</script>

<style>
	/* All CSS of this app or component */
</style>