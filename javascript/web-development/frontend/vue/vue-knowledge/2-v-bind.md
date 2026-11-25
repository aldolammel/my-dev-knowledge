#### JavaScript > Front-end > Vue
# Directive: `v-bind`

---

==For Vue-Router project==
Don't use `v-bind`. More info further below.

---

**It's accepted for:**
- any (with arg), obj (without arg).

**It's shorter caller:**
- `:` (colon)

You can apply v-bind using `v-bind` (or just `:`) before an attribute for example:

Calling URL:
```html
<!-- regular way: -->
<img src="https://somedomain.com/image.png" />
<!-- or using v-bind: -->
<img :src="p.image" />
```

---
## Using `v-bind` in hyperlinks:
Template literals:
```html
<a :href="`${post.slug}`">...
<a :href="`/user/${userId}/posts`">...
```
Concatenating strings:
```html
<a :href="'/user/' + userId">...
```
 With conditional:
```html
<a :href="isExternal ? externalUrl : internalUrl">Dynamic Link</a>

<!--
	In other words:
	
	if isExternal is true:
		use externalUrl
	otherwise:
		use internalUrl
-->
```

---
## Don't use `v-bind` if the front-end uses [Vue-Router](/javascript/web-development/frontend/vue/component-libraries/vue-router/_about.md):
Instead, you use `<router-link>`:
E.g. from this:
```html
<a :href="`/t/${tag.slug}`">...
```
To this:
```html
<router-link :to="`/t/${tag.slug}`">...
```

---
# Using `v-bind` to deactivate a button:

```html
<button
  :disabled="product.quantity <= 1"
  ...
>
	Remove
</button>
```

---
## Including a CSS-Class dynamically:

```html
<div
	class="menu-link"
	:class="{ selected : product.active }"
>
<!-- Output if menu-link is selected: class="menu-link selected" -->
```

---


