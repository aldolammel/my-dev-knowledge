// THIS FILE: /project_django/frontend/src/router/routes.js

// Component registry for lazy loading:
const componentRegistry = {
  // For static routes:
  SysNotFound: () => import("@/components/pages/SysNotFound.vue"),
  // For dynamic routes:
  Home: () => import("@/components/pages/Home.vue"),
  //About: () => import("@/components/pages/About.vue"),
};

// Static routes configuration:
const routes = [
  {
    path: "/oops", // TODO implementar isso!
    component: componentRegistry["SysNotFound"],
  },
  // TODO: 503 tambem
];

export { routes, componentRegistry };
