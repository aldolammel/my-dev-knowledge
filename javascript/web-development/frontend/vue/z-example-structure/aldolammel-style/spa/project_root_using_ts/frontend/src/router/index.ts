import { createRouter, createWebHistory } from "vue-router";
import type { RouteRecordRaw } from "vue-router";

// Route Views:
import HomePublicView from "@/views/public/HomeView.vue";
import AboutView from "@/views/public/AboutView.vue";
import TermsView from "@/views/public/TermsView.vue";
import RegisterView from "@/views/public/RegisterView.vue";
import LoginView from "@/views/public/LoginView.vue";

// Defining Route paths:
const routes: RouteRecordRaw[] = [
  {
    path: "/",
    //name: "Home",
    component: HomePublicView,
  },
  {
    path: "/about",
    //name: "About",
    component: AboutView,
  },
  {
    path: "/terms",
    //name: "Terms of Use",
    component: TermsView,
  },
  {
    path: "/register",
    //name: "Register",
    component: RegisterView,
  },
  {
    path: "/login",
    //name: "Login",
    component: LoginView,
  },
];

// Create router instance:
const router = createRouter({
  // Use HTML5 history mode (removes # from URLs)
  history: createWebHistory(import.meta.env.VITE_ROUTER_BASE),
  routes,
});

// Optional: Add global navigation guards:
router.beforeEach((to, from) => {
  // Example: Check authentication for protected routes
  if (to.meta.requiresAuth && !isAuthenticated()) {
    return "/login";
  }
});

// Helper function (example):
function isAuthenticated(): boolean {
  // Your authentication logic here!
  return localStorage.getItem("auth_token") !== null;
}

export default router;
