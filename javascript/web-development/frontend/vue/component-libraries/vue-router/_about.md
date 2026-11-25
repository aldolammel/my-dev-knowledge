#### JavaScript > Front-end > Vue > Components & Libraries
# Vue Router

---

Vue Router is the official client-side routing solution for Vue. Client-side routing is used by Single-Page Apps ([SPA](javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture.md)) to tie the browser URL to the content seen by the user. As users navigate around the app, the URL updates accordingly, but the page doesn't need to be reloaded from the server.

https://router.vuejs.org/

**Different URL's without browser reloading:**
E.g.
- https://domain.com/
- https://domain.com/about
- https://domain.com/products/biketrial
- etc

**E.g. of routers on app main menu:**
- Each menu link must be using the `<RouterLink>` tag (open and close the tag).
- Define with `<RouterView />` tag where the menu link's content (views) will be visualized.
```html
<!-- Navigation menu -->
<ul>
	<li>
		<RouterLink to="/">
			Home (It's a View)
		</RouterLink>
	</li>
	<li>
		<RouterLink to="/about">
			About (It's a View)
		</RouterLink>
	</li>
	<li>
		<RouterLink to="/contact">
			Contact (It's a View)
		</RouterLink>
	</li>
</ul>

<!-- Where each View is rendered when its RouterLink is clicked: -->
<RouterView />
```

---
## Data-flow diagram of a real Vue-Router usage in Django project:
[/python/web-development/django/useful-sub-apps/pagex/docs/django-with-vue-integration.excalidraw](/python/web-development/django/useful-sub-apps/pagex/docs/django-with-vue-integration.excalidraw)

---
## Installing:
[/javascript/web-development/frontend/vue/component-libraries/vue-router/_install](javascript/web-development/frontend/vue/component-libraries/vue-router/_install.md)
