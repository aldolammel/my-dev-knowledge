import { createRouter, createWebHistory } from "vue-router";

// Route Views > Public:
import HomePublicView from "@/views/public/HomeView.vue";
import AboutView from "@/views/public/AboutView.vue";
import TermsView from "@/views/public/TermsView.vue";
import RegisterView from "@/views/public/RegisterView.vue";
import LoginView from "@/views/public/LoginView.vue";
// Route Views > Authenticated:
// Reserved space...
// Route Views > System:
import EmailConfirmedView from "@/views/sys/EmailConfirmedView.vue";
import ForbiddenView from "@/views/sys/ForbiddenView.vue";
import NotFoundView from "@/views/sys/NotFoundView.vue";
import PwdForgottenView from "@/views/sys/PwdForgottenView.vue";

// Defining Route paths:
const routes: RouteRecordRaw[] = [
  // PUBLIC VIEWS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
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
  // LOGGED VIEWS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  // Reserved space...
  // SYSTEM VIEWS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  {
    path: "/confirmed",
    //name: "Email Confirmed",
    component: EmailConfirmedView,
  },
  {
    path: "/401",
    //name: "Access Forbidden (401)",
    component: ForbiddenView,
  },
  {
    path: "/404",
    //name: "Page Not Found (404)",
    component: NotFoundView,
  },
  {
    path: "/password_forgotten",
    //name: "Password Forgotten",
    component: PwdForgottenView,
  },
];

// Create router instance:
const router = createRouter({
  // Use HTML5 history mode (removes # from URLs)
  history: createWebHistory(import.meta.env.VITE_ROUTER_BASE),
  routes,
});

// Optional: Add global navigation guards:
router.beforeEach((to, from, next) => {
  // Example: Check authentication for protected routes
  if (to.meta.requiresAuth && !isAuthenticated()) {
    next("/login");
  } else {
    next();
  }
});

// Helper function (example):
function isAuthenticated() {
  // Your authentication logic here!
  return localStorage.getItem("auth_token") !== null;
}

export default router;