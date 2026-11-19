File: `/frontend/src/router/index.ts`:
```ts

import { createRouter, createWebHistory } from "vue-router";
import type { RouteRecordRaw } from "vue-router";

// Route Pages/Views:
import PgHome from "../components/pages/Home.vue";
import PgAbout from "../components/pages/About.vue";

// Define your routes
const routes: RouteRecordRaw[] = [
  {
    path: "/",
    //name: "Home",
    component: PgHome,
  },
  {
    path: "/about",
    //name: "About",
    component: PgAbout,
  },
];

// Create router instance
const router = createRouter({
  // Use HTML5 history mode (removes # from URLs)
  history: createWebHistory(import.meta.env.VITE_ROUTER_BASE),
  routes,
});

// Optional: Add global navigation guards
router.beforeEach((to, from) => {
  // Example: Check authentication for protected routes
  if (to.meta.requiresAuth && !isAuthenticated()) {
    return "/login";
  }
});

// Helper function (example)
function isAuthenticated(): boolean {
  // Your authentication logic here
  return localStorage.getItem("auth_token") !== null;
}

export default router;

```

---
## This file in JavaScript version:
[javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/project_one/frontend/src/router/index-js](javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/project_one/frontend/src/router/index-js.md)






