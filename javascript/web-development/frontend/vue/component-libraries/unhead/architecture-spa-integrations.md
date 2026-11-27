#### JavaScript > Front-end > Vue > Components & Libraries > Unhead
# Integration Unhead for SPA architecture

---
## Before:
- SPA on Vue: [/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture](/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture.md)
- Assuming you already installed Unhead-Vue: [/javascript/web-development/frontend/vue/component-libraries/unhead/_install](/javascript/web-development/frontend/vue/component-libraries/unhead/_install.md)

---

**1.1) In the APP's JS config file (`main.ts` or `main.js`):**
```ts
// Importing:
//...
import { createHead } from "@unhead/vue/client";

// Declarations:
//...
const head = createHead()

// Installing Vue plugins:
//...
app.use(head)

//...
```

**1.2) For global `<head>`'s `<meta>`, be simple, set them in the app's index:**
In `/frontend/index.html`: [/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/spa/project_root_using_ts/frontend/index.html](/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/spa/project_root_using_ts/frontend/index.html)

**1.3) Give to every view (page) a custom title (and optionally a description) while the user navigates through the app without browser refreshing:**
E.g., `/frontend/src/views/public/HomeView.vue`:
```html
<script setup lang="ts">
import { useSeoMeta } from "@unhead/vue";

// Components:
// ...

// Custom HTML <head>:
const viewTitle = "Home";
const viewDesc = "Welcome to our website";
useSeoMeta({
	// Commonly used by browser tab and history, Google services:
	title: viewTitle,
	description: viewDesc,
	// Friendly for other services like Discord, LinkedIn, Facebook, X, WhatsApp:
	ogTitle: viewTitle,
	ogDescription: viewDesc,
});
</script>

<!-- ... -->
```
In case you need to call script and stuff: [/javascript/web-development/frontend/vue/component-libraries/unhead/useHead-vs-useSeoMeta](/javascript/web-development/frontend/vue/component-libraries/unhead/useHead-vs-useSeoMeta.md)

---
## Unhead integration for MPA:
[/javascript/web-development/frontend/vue/component-libraries/unhead/architecture-mpa-integration](/javascript/web-development/frontend/vue/component-libraries/unhead/architecture-mpa-integration.md)


