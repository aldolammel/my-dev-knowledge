#### JavaScript > Front-end > Vue > Initial development
# Component approches

---

There are 2 ways to create Vue scripts, and them are called **Options API** and **Composition API**. Beyond the code changes, also the order of the Vue layers in the `.vue` files changes too:

**Options API** approach uses:
1. `<template>`
2. `<script>`
3. `<style>`

**Composition API** approach uses:
1. `<script>`
2. `<template>`
3. `<style>`

---
## OPTIONS API:

It's a way to define Vue components using an object with predefined option properties. The code is organized by options (data, methods, computed, etc.). It's the best way for Vue beginners.

**Conventions:**
- Component layers follow the order: template, script, style;

**Examples:**
- [/javascript/web-development/frontend/vue/vue-knowledge/using-options-api/\_example-1.vue](/javascript/web-development/frontend/vue/vue-knowledge/using-options-api/_example-1.vue)
- [/javascript/web-development/frontend/vue/vue-knowledge/using-options-api/\_example-2.vue](/javascript/web-development/frontend/vue/vue-knowledge/using-options-api/_example-2.vue)

**More about (folder):**
Same folder where the examples above are.

---
## COMPOSITION API:

The modern script syntax that is more concise and recommended approach for Vue 3, bringing flexibility for mid and large projects. It's much more close to the JS;

- The reactivity of template layer's elements need to be declared on script layer;
- xxxxxx
- xxxxxxxx

**Conventions:**
- Component layers follow the order: script, template, style;
- `ref()` only for primitives, `reactive()` only for objects;

**Examples:**
- [/javascript/web-development/frontend/vue/vue-knowledge/using-composition-api/\_example-1.vue](/javascript/web-development/frontend/vue/vue-knowledge/using-composition-api/_example-1.vue)
- [/javascript/web-development/frontend/vue/vue-knowledge/using-composition-api/\_example-2.vue](/javascript/web-development/frontend/vue/vue-knowledge/using-composition-api/_example-2.vue)

**More about (folder):**
Same folder where the examples above are.

---




