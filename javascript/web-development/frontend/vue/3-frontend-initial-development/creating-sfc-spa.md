#### JavaScript > Front-end > Vue > Initial development
# Creating a SFC (for SPA)

---
## Before:
- What is SPA: [/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture](/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture.md)

---
## 1) Where to create the SFC:
In `/frontend/src/views/one-sub-folder/NameHereView.vue` (that 'View' as suffix before the extension is a convention!)

Sub-folders logic:
- `/public/` for all pages that everyone can visit.
- `/logged/` for those pages that only authenticated users can access.
- `/sys/` for pages that are system response of something.

---
## 2) Simple view (minimal):
Using [Composition API](/javascript/web-development/frontend/vue/3-frontend-initial-development/component-approaches.md) approach:
```html
<script setup lang="ts">
// Components:
// Reserved space...
  
// Custom HTML <head>:
// Reserved space...
</script>

<template>
	<h1>My minimal view</h1>
</template>
  
<style scoped></style>

```

---
## 3) Adding a title and description SEO-friendly:
3.1) You need Vue-Unhead dependency: [/javascript/web-development/frontend/vue/component-libraries/unhead/\_install](/javascript/web-development/frontend/vue/component-libraries/unhead/_install.md)
3.2) Integrate it for SPA architecture: [/javascript/web-development/frontend/vue/component-libraries/unhead/architecture-spa-integrations](/javascript/web-development/frontend/vue/component-libraries/unhead/architecture-spa-integrations.md)

---
## 4) Adding a route for this view:

xxxxxxxxxxxxxxxxxxx

When a view is a parent of other views (children), probably you need to use nested routes in `/router/index.ts.` It requests from every view parent a `<RouterView />` in SFCs `<template>` layer, otherwise the child content won't be rendered. 

Nested Route VS Parent and Child SFCs: [/javascript/web-development/frontend/vue/3-frontend-initial-development/nested-routes-vs-parent-sfc](/javascript/web-development/frontend/vue/3-frontend-initial-development/nested-routes-vs-parent-sfc.md)


---

## 5) Adding a navigation menu:

xxxxxxxxxxxxxxxxxxxx

---
## X) Test it:
[/javascript/web-development/frontend/vue/vue-knowledge/_running-app](/javascript/web-development/frontend/vue/vue-knowledge/_running-app.md)

---




