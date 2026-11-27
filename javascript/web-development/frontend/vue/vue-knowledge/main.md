#### JavaScript > Front-end > Vue > Basic files
# Vue init file: `main.js`

---

The `main.js` is where the Vue is initiated, so it's crucial to call the `main.js` in the main app's HTML (`/frontend/index.html`).

---
## Minimal version:
In `/frontend/src/main.js` or `.ts`:
```ts
import { createApp } from "vue";
import App from "./App.vue"; // By convention, the main SFC (.vue) is called "App.vue".

// In mount() function is where Vue finally build up the app:
createApp(App).mount("#app");
```

---
## Real projects version:
[/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/spa/project_root_using_ts/frontend/src/main.ts](/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/spa/project_root_using_ts/frontend/src/main.ts)




