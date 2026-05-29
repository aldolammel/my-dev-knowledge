// THIS FILE: /project_django/frontend/src/router/router.js

import { createRouter, createWebHistory } from "vue-router";
import { routes, componentRegistry } from "@/router/routes"; // Bringing Vue Component pages and static routes!
import { usePagesStore } from "@/stores/pages"; // Vue Pinia
import { env } from "@/utils/env"; // Debug purposes

// Create the router instance:
const router = createRouter({
  history: createWebHistory(import.meta.env.VITE_ROUTER_BASE),
  routes,
});

// Dynamic routes initialization function:
export async function initDynamicRoutes() {
  const store = usePagesStore();
  const pages = await store.fetchAllPages();

  // Fetch each page and add their slug as a new route, storing them as Props, not as parameters:
  pages.forEach((page) => {
    const componentLoader = componentRegistry[page.vue_component];
    if (componentLoader) {
      // Adding the page slug as a new route:
      router.addRoute({
        path: `/${page.slug}`,
        component: componentLoader,
        props: { slug: page.slug },
      });
      if (page.is_home) {
        router.addRoute({
          path: "/",
          component: componentLoader,
          props: { slug: page.slug },
        });
      }
    } else {
      console.error(`FRONTEND ERROR > router.js: there's NO '${page.vue_component}' component!`);
    }
  });

  // Debug:
  if (env.isDebug) {
    console.debug(
      "FRONTEND DEBUG > router.js > Routes (statics + dynamics) available:",
      router.getRoutes()
    );
  }
}

export default router;
