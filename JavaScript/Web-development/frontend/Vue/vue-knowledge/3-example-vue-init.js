// By convention, this file is called and located: /src/main.js

import { createApp } from 'vue'
import App from './App.vue'  // By convention, the main .vue file is called App.vue.

// this '.mount' is where Vue must create the app:
createApp(App).mount('#app')

// Remember: this main.js file is called through index.html, that's why .mount knows where is
//            that 'app' ID.