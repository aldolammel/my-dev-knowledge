// Component registry for lazy loading:
const componentRegistry = {
  // For static routes:
  SysNotFound: () => import("@/components/pages/SysNotFound.vue"),
  // For dynamic routes:
  Home: () => import("@/components/pages/Home.vue"),
  About: () => import("@/components/pages/About.vue"),
  Profiles: () => import("@/components/pages/Profiles.vue"),
  Cannabis: () => import("@/components/pages/Cannabis.vue"),
  Test: () => import("@/components/pages/Test.vue"),
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
