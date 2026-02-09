// main.js used for real projects example:
// .../Vue/z-example-structure/aldolammel-style/frontend/src/main.js

// By convention, this file is located and called: /src/main.js

// Simplest example:

import { createApp } from "vue";
import App from "./App.vue"; // By convention, the main .vue file is called App.vue.

// this '.mount' is where Vue must create the app:
createApp(App).mount("#app");

// Remember: this main.js file is called through index.html, that's why .mount knows where is
//            that 'app' ID.
