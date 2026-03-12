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
};
// Static routes configuration:
const routes = [
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
