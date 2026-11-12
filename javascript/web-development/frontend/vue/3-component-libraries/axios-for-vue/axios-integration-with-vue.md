#### JavaScript > Vue
# Integrating Axios with Vue

---
## Before:
- Assuming you already installed Axios: [/javascript/nodejs/component-libraries/axios-api/axios](/javascript/nodejs/component-libraries/axios-api/axios.md)

---
## 1) Integration: 

### For SPA projects
1.1) In `/frontend/.env` file (DON'T in back-end `.env`), add these lines below. Case you need a front-end's `.env` file: [/environment-variables/env-for-local/in-frontend/env](/environment-variables/env-for-local/in-frontend/env.md)
```python
VITE_PROD_BASE_URL=https://client-main-domain.com
# Under Production, replace it by VITE_PROD_BASE_URL value!
VITE_BASE_URL=http://localhost:<django port>
```

==CRITICAL:==
Vue with Vite mandatorily requires env vars with `VITE_` prefix!

1.2) In the `/frontend/src/main.js` (or `main.ts`) file, include it:
```js
// Importing:
...
import axios from 'axios';

// Declarations:
...

// Other configs:
// Vite automatically searches for VITE_ prefix env vars:
axios.defaults.baseURL = import.meta.env.VITE_BASE_URL;  // Where Django's running currently!

// Installing Vue plugins:
...
```

......................................

### For MPA projects
x) xxxx
x) xxxx
x) xxxx

---



