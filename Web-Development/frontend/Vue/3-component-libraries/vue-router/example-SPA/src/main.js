// FILE: /frontend/src/main.js

import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // Import your router config (/frontend/src/router/index.js)

// Create Vue application instance
const app = createApp(App)

// Use the router plugin
app.use(router)

// Mount the application
app.mount('#app')