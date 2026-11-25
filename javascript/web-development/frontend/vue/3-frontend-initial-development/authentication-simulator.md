#### JavaScript > Front-end > Vue > Initial development
# Authentication simulator

---
## Before:
- [x] This temporary solution makes sense only before the [Pinia](/javascript/web-development/frontend/vue/component-libraries/pinia/_install.md) implementation and just for development test purposes.
- [x] Assuming you are using some kind of front-end local `.env` file: [/environment-variables/env-for-local/in-frontend/env](/environment-variables/env-for-local/in-frontend/env.md)
- [x] Assuming you are using [Vite](/javascript/build-tools/vite/_install.md) as JS build-tool.

---
## Quick review about Vue auth logic work-flow:
- [x] [/javascript/web-development/frontend/vue/component-libraries/pinia/authentication-workflow](/javascript/web-development/frontend/vue/component-libraries/pinia/authentication-workflow.md)

---
## 1) Create `.env` var to simulate user authentication:
- [x] In `/frontend/.env` or  something like`/frontend/.env.development.local`:
```python
VITE_DEBUG=true

# For initial front-end auth tests without Pinia:
VITE_LOCAL_FAKE_USER_LOGGED=true

#...
```

---
## 2) Create or edit the `useAuth` file:
For now, this is the single source of truth for your temporary authentication state (before to implement Pinia). 
- [x] In `/frontend/src/composables/useAuth.ts` (or `.js`):
```ts
// CRITICAL DEV SOLUTION: this user authentication is temporary before the Pinia implementation!
// When Pinia's implementated, it takes the data from /stores/auth.ts file!
export function useAuth() {
  const isAuthenticated =
    import.meta.env.VITE_DEBUG === "true" && import.meta.env.VITE_LOCAL_FAKE_USER_LOGGED === "true";
  return {
    isAuthenticated,
  };
}
```

---
## 3) Make sure the `guards.ts` is set to deal with `useAuth.ts`:
No matter if the authentication is fake in this roadmap, for `guards.ts`, if `useAuth` tells the user is authenticated, this is true.
- [x] In `/frontend/src/router/guards.ts`:
```ts
import type { Router } from "vue-router";
import { useAuth } from "@/composables/useAuth";

// Register global navigation guards:
export function registerNavigationGuards(router: Router): void {
	// registerNavigationGuards() avoids circular dependencies between index.ts and guards.ts!
	router.beforeEach(to => {
		const { isAuthenticated } = useAuth();
	
		if (to.meta.requiresAuth && !isAuthenticated) {
			return {
				name: "Login",
				query: { redirect: to.fullPath },
			};
		}
	});
}
```
For `.js` version:
```js
// Do it yourself ;)
```

---
## 4) Import the registration function in router:
- [x] 4.1) In `/frontend/src/router/index.ts` import the `guards` file:
```ts
//...
import { registerNavigationGuards } from "@/router/guards";

// Route Views:
//...
```
- [x] 4.2) Still in the same file, but right after the `router` var creation:
```ts
//...

// Create router instance:
//...

// Register navigation guards:
registerNavigationGuards(router);

//...
```

---
## 5) Make sure an app's menu is considering authenticated views/pages too:
- [x] In some `/frontend/src/components/navigation/` menu, use this example below to edit your menu.
```html
<script setup lang="ts">
import { useAuth } from "@/composables/useAuth";
const { isAuthenticated } = useAuth();
</script>

<template>
  <nav>
    <template v-if="isAuthenticated">
      <RouterLink :to="{ name: 'PageLoggedA' }">Logged page A</RouterLink>
    </template>

    <template v-else>
      <RouterLink :to="{ name: 'CreateAccount' }">Create account</RouterLink>
      <RouterLink :to="{ name: 'Login' }">Login</RouterLink>
    </template>

    <RouterLink :to="{ name: 'PagePublic1' }">Page Public 1</RouterLink>
    <a href="https://buymeacoffee.com/aldolammel">Donation</a>
  </nav>
</template>
```
==Tip:== call view's paths using their identifier, never their path directly! 

---
## 6) Test it, but:
- [x] 6.1) Make sure you are in the `/frontend/` folder
- [x] 6.2) (If applicable) Close the Node server.
- [x] 6.3) Close any terminal you were using front-end stuff.
- [x] 6.4) Open a new terminal to make sure the new `.env` var is loaded.
- [x] 6.5) Run the front-end server: [/javascript/web-development/frontend/vue/vue-knowledge/\_running-app](/javascript/web-development/frontend/vue/vue-knowledge/_running-app)

Done.

---




