#### JavaScript > Front-end > Vue > Components & Libraries > Unhead
# Integration Unhead for SPA architecture

---
## Before:
- SPA on Vue: [/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture](/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture.md)
- Assuming you already installed Unhead-Vue: [javascript/web-development/frontend/vue/component-libraries/unhead/_install](javascript/web-development/frontend/vue/component-libraries/unhead/_install.md)

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

**1.2) (Optional) Customizing global `<head>`'s `<meta>` in a way it's propagate through the entire app:**
In `/frontend/src/App.vue`:
```html
<script setup lang="ts">
import { useSeoMeta } from "@unhead/vue";

// Components:
// ...

// Custom HTML <head>:
useSeoMeta({
	// Global customs for all views/pages:
	author: "Your Name",
});
</script>

<!-- ... -->
```
In case you need to call script and stuff: [/javascript/web-development/frontend/vue/component-libraries/unhead/useHead-vs-useSeoMeta](/javascript/web-development/frontend/vue/component-libraries/unhead/useHead-vs-useSeoMeta.md)

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

---
## Unhead integration for MPA:
[javascript/web-development/frontend/vue/component-libraries/unhead/architecture-mpa-integration](javascript/web-development/frontend/vue/component-libraries/unhead/architecture-mpa-integration.md)


