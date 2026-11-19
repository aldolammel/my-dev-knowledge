#### JavaScript > Front-end > Vue > Components & Libraries
# Vue Router: installation and integration

---

==For MPA project: DON'T!==
In a MPA architecture, the browser handles navigation by requesting a completely new HTML page from the back-end on every link click. Because there is only one page active at any given moment, client-side routing (Vue Router) is unnecessary!

---
## Before:
- [x] Assuming your project is a SPA: [/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture](/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture.md)

---
## 1) Installing:

==If using the build-tool Vue-CLI==
If you already created your project via [Vue-CLI](/javascript/web-development/frontend/vue/build-tools/vue-cli/_about.md) (default), you probably already have the Router once it was an Vue-CLI option during the project creation process. Make sure about checking it through the Vue project folder:
```bash
npm list
# or:
npm list vue-router
```
If you don't see any router stuff, keep with the installation and integration processes below, otherwise skip this roadmap!

- [x] To install Vue-Router:
```bash
# Specific version:
npm install vue-router@<version you want>
# Or the latest one:
npm install vue-router@latest
```
- [x] Check installation:
```bash
npm list vue-router
```
Uninstall (if needed): [/javascript/web-development/frontend/vue/component-libraries/vue-router/router-uninstall](/javascript/web-development/frontend/vue/component-libraries/vue-router/router-uninstall.md)

---
## 2) (If applicable) Create the front-end's `.env` file:
- [x] 2.1) Create an exclusive `.env` file to set the front-end environment variables: [/environment-variables/env-for-local/in-frontend/env](/environment-variables/env-for-local/in-frontend/env.md)
- [x] 2.2) Don't forget to rename the `.env` variables to be compatible with Vite.
- [x] 2.3) (Optional) Make sure this new `.env` is ignored by [Git](/versioning/git/_basic.md). This line should be there: `frontend/.env`

---
## 3) Integration:
- [x] 3.1) In the `/frontend/.env` file, create these env vars if not yet: [/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/project_one/frontend/env_example](/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/project_one/frontend/env_example.md)
- [x] 3.2) Import the router in the `main.js` (or `main.ts`) file: [/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/project_one/frontend/src/main.js](/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/project_one/frontend/src/main.js)
- [x] 3.3) Create the router-config file and setup its options:
	- Case using JS: [/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/project_one/frontend/src/router/index-js](/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/project_one/frontend/src/router/index-js.md)
	- Case using TS: [/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/project_one/frontend/src/router/index-ts](/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/project_one/frontend/src/router/index-ts.md)
- [ ] 3.4) (Optional) Make sure you already have all views "pages" in `.vue` files in the `/frontend/src/pages/` folder. Don't develop those pages now, but create them.
- [ ] 3.5) Define where all views ("pages") must be rendered in your front-end template, adding this where each View must be loaded: `<RouterView />` (e.g., [/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/project_one/frontend/src/App.vue](/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/project_one/frontend/src/App.vue)).
- [ ] 3.6) Define each link option (`<RouterLink>`) for the main navigation menu of the app. E.g.: [/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/project_one/frontend/src/components/NavMain.vue](/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/project_one/frontend/src/components/NavMain.vue)

---
## 4) Testing:
[/javascript/web-development/frontend/vue/vue-knowledge/\_running-app](/javascript/web-development/frontend/vue/vue-knowledge/_running-app.md)


        
                
