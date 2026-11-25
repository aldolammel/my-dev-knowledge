#### JavaScript > UI component library
# Vuetify

---

Vuetify is a [Vue.js](/javascript/web-development/frontend/vue/_about.md) component framework that implements "Material Design" (a Design System by Google) specification. It's essentially a comprehensive UI library for building Vue apps with Material Design aesthetics and principles.

https://vuetifyjs.com

---
## 1) Installation:

- [x] **Before:**
- Assuming you are in the `/frontend/` folder of the project.
- (If applicable) For Node installation with version control, active the specific Node for this project: [/javascript/web-development/backend/nodejs/activating-node-specific-version](javascript/web-development/backend/nodejs/activating-node-specific-version.md)
- (If applicable) Assuming you're in the right Git branch: [command-branch](/versioning/git/command-branch.md) and [command-checkout](/versioning/git/command-checkout.md).
.
- [x] 1.1) Install the Vuetify itself:
```bash
# npm:
npm install vuetify
```

- [x] 1.2) Integration with the project's build-tool:

**Using Vite:**
```bash
# npm:
npm install -D vite-plugin-vuetify
```

- [x] 1.3) (Optional) Installing the Material Design Icons font (RECOMMENDED):
```bash
npm install @mdi/font
```

---
## 2) Define Vuetify versions range for future updates:
- [ ] In `/frontend/package.json` define the limit version for Vuetify updates (it should be declared in the project's [TDD](/javascript/document-templates/techical-design-document-tdd.md)):
```json
{
	//...
	"dependencies": {
		//...
		"vuetify": ">=4.3.4 <5.0.0",
	}
}
```


---
## 3) Integration:

**Using Vite as build-tool:**

- [x] 3.1) Making Vuetify be able to import components automatically:
In `vite.config.ts` (or `.js`):
```ts
//...
import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'

export default defineConfig({
  plugins: [
    vue({
      template: { transformAssetUrls },
    }),
    vuetify({
      autoImport: true,
    }),
  ],
  //...
});
```

- [x] 3.2) Configuring Vuetify:
Create `/frontend/src/libs/vuetify.ts` (or `.js`):
```ts
import '@mdi/font/css/materialdesignicons.css'  // Case you have installed the @mdi/font!
import 'vuetify/styles'

import { createVuetify } from 'vuetify'

export default createVuetify({
  theme: {
    defaultTheme: 'light',
  },
})
```

- [x] 3.3) Registering Vuetify:
In `/frontend/src/main.ts` or `.js`:
```ts
// Importing:
//...
import vuetify from '@/libs/vuetify'

// Installing Vue plugins:
//...
app.use(vuetify)

//...
```

---



