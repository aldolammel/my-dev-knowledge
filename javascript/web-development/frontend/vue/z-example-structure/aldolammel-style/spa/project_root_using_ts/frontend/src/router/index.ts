import { createRouter, createWebHistory } from "vue-router";
import type { RouteRecordRaw } from "vue-router";

// Layouts:
import PublicLayout from "@/layouts/PublicLayout.vue";
// import LoggedLayout from "@/layouts/LoggedLayout.vue";

// Route Views > Public:
import HomePublicView from "@/views/public/HomePublicView.vue";
import SupportView from "@/views/public/SupportView.vue";
import TermsView from "@/views/public/TermsView.vue";
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
    component: PublicLayout,
    children: [
      {
        path: "",
        name: "HomePublic", // It's not a title, but an identifier using PascalCase.
        component: HomePublicView,
      },
      {
        path: "support",
        name: "Support",
        component: SupportView,
      },
      {
        path: "terms",
        name: "Terms",
        component: TermsView,
      },
      {
        path: "login",
        name: "Login",
        component: LoginView,
      },
    ],
  },
  // LOGGED VIEWS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  // {
  //   path: "/",
  //   component: LoggedLayout,
  //   meta: { requiresAuth: true },
  //   children: [
  //     {
  //       path: "xxxxxx",
  //       name: "SomethingLikeThis", // It's not a title, but an identifier using PascalCase.
  //       component: XxxxView,
  //     },
  //     {
  //       path: "xxxxxx",
  //       name: "xxxxxx",
  //       component: XxxxView,
  //     },
  //   ],
  // },
  // SYSTEM VIEWS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  {
    path: "/confirmed",
    name: "EmailConfirmed", // It's not a title, but an identifier using PascalCase.
    component: EmailConfirmedView,
  },
  {
    path: "/401",
    name: "AccessForbidden",
    component: ForbiddenView,
  },
  {
    path: "/password_forgotten",
    name: "PwdForgotten",
    component: PwdForgottenView,
  },
  {
    path: "/404",
    name: "PageNotFound",
    component: NotFoundView,
  },
  {
    path: "/:pathMatch(.*)*",
    redirect: "/404",
  },
];

// Create router instance:
const router = createRouter({
  // Use HTML5 history mode (removes # from URLs)
  history: createWebHistory(import.meta.env.VITE_ROUTER_BASE),
  routes,
});

export default router;
