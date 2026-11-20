#### JavaScript > Front-end > Vue > Components & Libraries > Unhead
# `useHead()` vs `useSeoMeta()`

---
## Before:
- What is Unhead-Vue: [/javascript/web-development/frontend/vue/component-libraries/unhead/\_install](/javascript/web-development/frontend/vue/component-libraries/unhead/_install.md)

---
## Use `useSeoMeta()` for:
HTML head's customization of:
- title
- description
- author
- Open Graph
- X (Twitter).

E.g. in a `.vue` file:
```html
<script setup lang="ts">
useSeoMeta({
	// Commonly used by browser tab and history, Google services:
	title: "Home",
	description: "Welcome",
	// Friendly for other services like Discord, LinkedIn, Facebook, X, WhatsApp:
	ogTitle: "Home",
	ogDescription: "Welcome",
});
</script>
```

---
## Use `useHead()` for:
HTML head's customization of:
- links
- scripts
- JSON-LD
- htmlAttrs
- Any meta name that is not in that flat list.

E.g. in a `.vue` file:
```html
<script setup lang="ts">
useHead({
  link: [{ rel: "canonical", href: "https://example.com/" }],
});
</script>
```

---
## Both can be called in the same component:
```html
<script setup lang="ts">

useHead({
	...
});

useSeoMeta({
	...
});

</script>
```

---
