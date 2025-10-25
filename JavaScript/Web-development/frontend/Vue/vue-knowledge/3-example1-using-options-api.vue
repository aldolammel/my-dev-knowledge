<!-- 
  
  Using the "Options API" approach:
  More about: ./using-options-api/

-->


<!--
	
	Vue app starts when index.html calls the Vue init file:
		./3-example-main-html.html

	Vue init file:
		./3-example-vue-init.js

-->

<!-- By convention, in Options API approach, template layer should be the first layer -->
<template>
</template>

<script>
	// Importing things:
	// Reserved space...

	export default {
		// This Current file/component name (optional but recommended)
		name: 'ThisComponentName',

		// This component children's registration:
		components: {
			//ChildComponentNameOne,
			//MyChild: ChildComponentNameTwo,  // To use on the component a different name of file's name.
			//ChildComponentNameThree
		},

		// Component state/data
		data() {
			// 'return' here always need to return an JS obj "{}":
			return {
				// Piece of data that Vue is aware of:
				myString: 'Hello World',  // ...... storing a string.
				myArray: ['one', 'two'], // ....... storing an array.
				myBool: true,  // ................. storing a boolean.
				myNum: 123,  // ................... storing an integer.
				myObj: {}  // ..................... storing an object.
			}
		},

		// Methods/functions
		// /JavaScript/Web-development/frontend/Vue/vue-knowledge/using-options-api/_option-methods.vue
		methods: {
			updateMessage() {
				this.myString = 'Updated!'
			}
		}
	}
</script>

<style>
	/* All CSS of this component */
</style>