#### JavaScript > Front-end > Vue > Initial development
# Authentication simulator

---
## Before:
- [x] Assuming you are using some kind of front-end local `.env` file: [/environment-variables/env-for-local/in-frontend/env](/environment-variables/env-for-local/in-frontend/env.md)

---
## 1) Create `.env` var to simulate user authentication:
- [x] In `/frontend/.env` or  something like`/frontend/.env.development.local`:
```
#...

# Only for development:
LOCAL_FAKE_USER_LOGGED=true

#...
```

---
## 2) **Add the fake authentication guard**:
- [x] In `/frontend/src/router/guards.ts`:
```ts
import type { Router } from "vue-router";

// Temporary authentication simulation:
// TODO: when Pinia authentication is implemented, replace this func with the actual authentication store state!
function isAuthenticated(): boolean {
	return import.meta.env.LOCAL_FAKE_USER_LOGGED === "true";
}

// Register global navigation guards:
// This func receives the router instance instead of importing it, avoiding circular dependencies between index.ts and guards.ts:
export function registerNavigationGuards(router: Router): void {
	router.beforeEach(to => {
		if (to.meta.requiresAuth && !isAuthenticated()) {
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
## 3) Import the registration function in router:
- [x] 3.1) In `/frontend/src/router/index.ts` import the `guards` file:
```ts
//...
import { registerNavigationGuards } from "@/router/guards";

// Route Views:
//...
```
- [x] 3.2) Still in the same file, but right after the `router` var creation:
```ts
//...

// Create router instance:
//...

// Register navigation guards:
registerNavigationGuards(router);

//...
```

---
## 4) Restart the front-end project:
- [x] 4.1) (If applicable) Close the Vue server.
- [x] 4.2) Close any terminal you were using front-end stuff.
- [x] 4.3) Open a new terminal to make sure the new `.env` var is loaded.

---
## 5) (If applicable) Test:
Maybe you are not ready to test it because xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

If you are ready: 
- Make sure you are in the `/frontend/` folder
- Run the front-end server: [/javascript/web-development/frontend/vue/vue-knowledge/\_running-app](/javascript/web-development/frontend/vue/vue-knowledge/_running-app)

---




