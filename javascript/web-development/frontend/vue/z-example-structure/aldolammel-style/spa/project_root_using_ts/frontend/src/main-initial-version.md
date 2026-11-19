## Minimal Vue main file initialization:
Compatible with JavaScript (`main.js`) or TypeScript (`main.ts`) version:
```js
// Importing:
import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

// CSS globals:
// They're declared in HTML header!

// Declarations:
const app = createApp(App);

// Other configs:
// Reserved space...

// Installing Vue plugins:
// Reserved space... e.g. app.use(...)

// Finally, allowing app to be mounted in HTML:
app.mount("#app");
```

