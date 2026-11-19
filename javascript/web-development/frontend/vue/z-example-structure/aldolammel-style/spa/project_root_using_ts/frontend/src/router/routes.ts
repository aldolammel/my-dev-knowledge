
import type { Component } from "vue";
import type { RouteRecordRaw } from "vue-router";

// Component registry for lazy loading:
const componentRegistry = {
  // For static routes:
  LoadError: () => import("@/components/pages/LoadError.vue"),

  // For dynamic routes:
  Home: () => import("@/components/pages/Home.vue"),
  About: () => import("@/components/pages/About.vue"),
  LoadBlog: () => import("@/components/pages/LoadBlog.vue"),
  LoadBlogPost: () => import("@/components/pages/LoadBlogPost.vue"),
  ListByCategory: () => import("@/components/pages/ListByCategory.vue"),
  ListByTag: () => import("@/components/pages/ListByTag.vue"),
} satisfies Record<string, () => Promise<Component>>;

// Static routes configuration:
const routes: RouteRecordRaw[] = [
  {
    path: "/:pathMatch(.*)*", // Catch unregistered routes!
    component: componentRegistry["LoadError"],
  },
  {
    path: "/503",
    component: componentRegistry["LoadError"],
  },
];

export { routes, componentRegistry };
