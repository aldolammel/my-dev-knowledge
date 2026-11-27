import { createRouter, createWebHistory } from "vue-router";
import type { RouteRecordRaw } from "vue-router";

// Declared Types:
// In @/types/vue-router.d.ts

// Defining Route paths:
const routes: RouteRecordRaw[] = [
  // PUBLIC VIEWS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  {
    path: "/",
    component: () => import("@/layouts/PublicLayout.vue"),
    children: [
        {
            path: "",
            name: "HomePublic", // It's an identifier (PascalCase) used to call the view path on templates! Use the component name without 'View'.
            component: () => import("@/views/public/HomePublicView.vue"),
        },
        {
            path: "about",
            name: "About",
            component: () => import("@/views/public/AboutView.vue"),
        },
        {
            path: "register",
            name: "Register",
            component: () => import("@/views/public/RegisterView.vue"),
            meta: { guestOnly: true },
        },
        {
            path: "login",
            name: "Login",
            component: () => import("@/views/public/LoginView.vue"),
            meta: { guestOnly: true },
        },
        {
            path: "terms",
            name: "Terms",
            component: () => import("@/views/public/TermsView.vue"),
        },
        // EXAMPLES HOW TO CREATE NESTED PAGES WITHOUT TO CREATE NESTED ROUTE (not recommended for cases like this):
        // https://github.com/aldolammel/my-dev-knowledge/tree/main/javascript/web-development/frontend/vue/3-frontend-initial-development/nested-routes-vs-parent-sfc.md
        {
            path: "blog",
            name: "Blog",
            component: () => import("@/views/public/BlogView.vue"),
        },
        {
            path: "blog/:postId",  // on browser it would be https://mysite.com/blog/23
            name: "BlogPost",
            component: () => import("@/views/public/BlogPostView.vue"),
            props: true,
        },
        // SYSTEM VIEWS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        {
            path: "confirmed",
            name: "EmailConfirmed", // It's an identifier (PascalCase) used to call the view path on templates! Use the component name without 'View'.
            component: () => import("@/views/sys/EmailConfirmedView.vue"),
        },
        {
            path: "401",
            name: "Forbidden",
            component: () => import("@/views/sys/ForbiddenView.vue"),
        },
        {
            path: "password_forgotten",
            name: "PwdForgotten",
            component: () => import("@/views/sys/PwdForgottenView.vue"),
        },
        {
            path: "404",
            name: "NotFound",
            component: () => import("@/views/sys/NotFoundView.vue"),
        },
        {
            path: ":pathMatch(.*)*",
            redirect: "404",
        },
    ],
  },
  // LOGGED VIEWS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  // {
  //   path: "/",
  //   component: () => import("@/layouts/LoggedLayout.vue"),
  //   meta: { requiresAuth: true },
  //   children: [
  //     {
  //       path: "",
  //       name: "HomeLogged", // It's an identifier (PascalCase) used to call the view path on templates! Use the component name without 'View'.
  //       component: () => import("@/views/logged/HomeLoggedView.vue"),
  //     },
  //     {
  //       path: "blog/new",  // on browser it would be https://mysite.com/blog/new
  //       name: "BlogPostCreate",
  //       component: () => import("@/views/logged/BlogPostCreateView.vue"),
  //     },
  //     {
  //       path: "blog/:postId/edit",  // on browser it would be https://mysite.com/blog/46/edit
  //       name: "BlogPostEdit",
  //       component: () => import("@/views/logged/BlogPostEditView.vue"),
  //       props: true,
  //     },
  //   ],
  // },
];

// Create router instance:
const router = createRouter({
  // Use HTML5 history mode (removes # from URLs)
  history: createWebHistory(import.meta.env.VITE_ROUTER_BASE),
  routes,
});

export default router;
