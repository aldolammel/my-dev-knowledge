#### JavaScript > Vue > Project types
# Vue app architectures observations

---
## Before:
- What is application architecture for web development and its types: [/dev-concepts/web-dev-app-architecture](/dev-concepts/web-dev-app-architecture.md)

---
## Static Site Generation (SSG):
Good opportunity to use [VitePress](/javascript/build-tools/vite/vitepress.md).
Or a full-stack solution that support SSG: Nuxt.js

---
## Single Page Application (SPA):
- Vue controls the entire app, including page rendering, navigation ([Vue Router](/javascript/web-development/frontend/vue/3-component-libraries/vue-router/_vue-router.md)), and application state ([Pinia](/javascript/web-development/frontend/vue/3-component-libraries/pinia/_install.md)).
- Poor compatible with SEO.
- Poor compatible with link previews (sharing content).

---
## Multi Page Application (MPA):
- Vue can enhance individual pages, but doesn't own the entire app as it would be in SPA.
- The browser handles navigation by requesting a completely new HTML page from the back-end on every link click, making the client-side routing (Vue Router) unnecessary.
- For Vue project following MPA architecture, is recommended to use [Nuxt.js](/javascript/web-development/frontend/vue/3-component-libraries/nuxt/_about.md) instead of just Vue.
- Full compatible with SEO.
- Full compatible with link previews (sharing content).

---
## Server-Side Rendering (SSR):
- Vue has no this capacity because Vue is a front-end framework. For complex projects that demand CMS you need a SSR like Django, 