#### JavaScript > Vue
# Vue knowledge

---
## Before:
- What is Vue: [/javascript/web-development/frontend/vue/vue-knowledge/\_about](/javascript/web-development/frontend/vue/vue-knowledge/_about.md)

---
## App architecture:
For every Vue project, it's crucial define which app architecture you will follow once it impacts the development needs: [/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture](/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture.md)

---
## Two main Vue cores:
In Vue, part of the work is done in JS file, and another part in the HTML file.

**Declarative Rendering:** 
Vue extends standard HTML with a template syntax that allows us to declaratively describe HTML output based on JavaScript state.

**Reactivity:**
Vue automatically tracks JS state changes and efficiently updates the DOM (Document Object Model) when changes happen.

---
## Vue core: Declarative Rendering:
It's the same as 'Template variable' in Django Templates, for example. You can use this only in HTML elements/tags, but never in their attributes (more about it, next).

E.g. 
```html
{{ my_template_var }}
```


>> DECLARATIVE RENDERING: FOR DYNAMIC ATTRIBUTES
If you need to use a Directive (more about it, next) in a HTML attribute, you cannot use
Declarative Rendering {{ }} but ":" as suffix of the attribute name. Like this example:

>> context:
You're using a for-loop that wanna call an image from db. Each product has an 'image' attribute with the string value:
"/img/<nameImage.fileType>"
```

<div v-for="p in products">
	<img src="/img/anyimage.gif">
</div>
```
		
>> from this:
```
<img src="/img/anyimage.gif">
```
		
>> to this:

			wrong:
```
<img src={{ p.image }}>
<img src="{{ p.image }}">
```

right (using v-bind abbreviation ":" before html-tag's attribute):
```
<img :src="p.image">
```


>> CONDITIONAL DECLARATIVE RENDERING

```
{{ book.isReady ? "I'm ready" : 'NOT READY YET' }}
```

---
## Single-File Components (SFC), `.vue`:
What is it: [/dev-concepts/sfc](/dev-concepts/sfc)

E.g.:
```vue
<script setup>
import { ref } from 'vue'
const greeting = ref('Hello World!')
</script>

<template>
  <p class="greeting">{{ greeting }}</p>
</template>

<style>
.greeting {
  color: red;
  font-weight: bold;
}
</style>
```
Convention layers orders in a `.vue` file based on the used code approach: [/javascript/web-development/frontend/vue/3-frontend-initial-development/component-approaches](/javascript/web-development/frontend/vue/3-frontend-initial-development/component-approaches.md)

---
## Vue folder structure:
[/javascript/web-development/frontend/vue/vue-knowledge/1-vue-structure](/javascript/web-development/frontend/vue/vue-knowledge/1-vue-structure.md)

---
## VUE DIRECTIVES:
[/javascript/web-development/frontend/vue/vue-knowledge/2-directives](/javascript/web-development/frontend/vue/vue-knowledge/2-directives.md)
## VUE APPs AND THEIR COMPONENTS
[/javascript/web-development/frontend/vue/vue-knowledge/5-components](/javascript/web-development/frontend/vue/vue-knowledge/5-components.md)


