// Importing for SPA:
import { createApp } from "vue";
import App from "@/App.vue";
import { createHead } from "@unhead/vue/client";
import router, { initDynamicRoutes } from "@/router/router";
import { createPinia } from "pinia";
import { useGlobalStore } from "@/stores/global";
import axios from "axios";

// CSS globals:
// They're declared in HTML header!

// Declarations:
const app = createApp(App);
const pinia = createPinia();
const head = createHead();

// Other configs:
axios.defaults.baseURL = import.meta.env.VITE_BASE_URL; // Where Django's running currently!

// Installing Vue plugins:
app.use(pinia);
app.use(head);

(async () => {
  try {
    // Initialize global info store first:
    const globalStore = useGlobalStore();
    await globalStore.initializeGlobal();
    // Wait for dynamic routes after global data is ready:
    await initDynamicRoutes();
    // Installing the router plugin:
    app.use(router);
    // Finally, allowing app to be mounted in HTML:
    app.mount("#app");
  } catch (error) {
    console.error("FRONTEND ERROR > App initialization failed:", error);
  }
})();
