#### JavaScript > Front-end > Vue > Initial development
# Nested Route VS Parent and Child SFCs

---
 
Sometimes, it's attractive to replicate a sitemap navigation in `/router/index.ts` just because there you see a nested route with many child routes, super organized. But that approach for every view probably is a mistake. Why? Because, for Vue Router, a children array means "*render this child inside the parent's* `<RouterView>`*!*"

Every page should be a flat child of a layout (e.g., `PublicLayout.vue`). The sitemap hierarchy lives in the URL structure (`/blog/:post/edit`), not in component nesting.

If the matter is not clear or you are not convinced about user or not nested routes to organize your app navigation, keep reading!
### The problem
E.g. sitemap:
```
mysite.com
├── Home
├── About
│   ├── Timeline
│   └── Photos
└── ...
```
Getting sitemap logic and replicating that to the front-end router (`/frontend/src/router/index.ts`): 
```ts
{
	path: "/",
	component: PublicLayout,
	children: [
		{
			path: "",
			name: "HomePublic",
			component: HomePublicView,
		},
		{
			// THE NESTED ROUTE I'M TALKING:
			path: "about",  // on browser, it would be: https://aldolammel.com/about
			name: "About",
			component: AboutView,
			// It looks a great idea but - maybe - it's not (see further below):
			children: [
				{
					path: "timeline",  // on browser, it would be: https://aldolammel.com/about/timeline
					name: "Timeline",
					component: TimelineView,
				},
			]
		},
	]
}
```
Once the `AboutView.vue` router is set as a nested route, now it demands a `<RouterView />` in its `<template>` layer. Why? Otherwise the users couldn't see `TimelineView.vue` content. 
E.g.: `AboutView.vue` (`mysite.com/about`):
```html
<script></script>

<template>
	<h1> ABOUT </h1>
	<p>My about content.</p>
	
	<RouterView /> <!-- <<<<<<<<<<<<<<<<<-------------------------- -->
	
</template>
```
Look how the app would be rendered when a user would visit `mysite.com/about/timeline`:
```
ABOUT
My about content.
TIMELINE
My timeline content.
```
Output: a weird content, completed mixed instead of a dedicated page for each one.
### Solution
```ts
{
	path: "/",
	component: PublicLayout,
	children: [
		{
			path: "",
			name: "HomePublic",
			component: HomePublicView,
		},
		{
			// THE NESTED ROUTE I'M TALKING:
			path: "about",  // on browser, it would be: mysite.com/about
			name: "About",
			component: AboutView,
		},
		{
			path: "about/timeline",  // on browser, it would be: mysite.com/about/timeline
			name: "Timeline",
			component: TimelineView,
		},
	]
}
```

---
