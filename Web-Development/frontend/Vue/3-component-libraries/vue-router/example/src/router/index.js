import { createRouter, createWebHistory } from 'vue-router'

// Import your route components
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'

// Define your routes
const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'About',
    // Lazy-loaded route component (code splitting)
    component: () => import('../views/AboutView.vue')
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import('../views/DashboardView.vue'),
    // Add route guards if needed
    meta: { requiresAuth: true }
  }
]

// Create router instance
const router = createRouter({
  // Use HTML5 history mode (removes # from URLs)
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

// Optional: Add global navigation guards
router.beforeEach((to, from, next) => {
  // Example: Check authentication for protected routes
  if (to.meta.requiresAuth && !isAuthenticated()) {
    next('/login')
  } else {
    next()
  }
})

// Helper function (example)
function isAuthenticated() {
  // Your authentication logic here
  return localStorage.getItem('auth_token') !== null
}

export default router