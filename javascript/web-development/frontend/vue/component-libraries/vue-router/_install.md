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
## 2) Define Vue-Router versions range for future updates:
In `/frontend/package.json` define the limit version for Vue-Router updates (it should be declared in the project's [TDD](/javascript/document-templates/techical-design-document-tdd.md)):
```json
{
	//...
	"dependencies": {
		//...
		"vue-router": ">=5.5.1 <6.0.0",
	}
}
```

---
## 3) (If applicable) Create the front-end's `.env` file:
- [x] 3.1) Create an exclusive `.env` file to set the front-end environment variables: [/environment-variables/env-for-local/in-frontend/env](/environment-variables/env-for-local/in-frontend/env.md)
- [x] 3.2) Don't forget to rename the `.env` variables to be compatible with Vite.
- [x] 3.3) (Optional) Make sure this new `.env` is ignored by [Git](/versioning/git/_basic.md). This line should be there: `frontend/.env`

---
## 4) Integration:
- [x] 4.1) In the `/frontend/.env` file, create these env vars if not yet: [/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/frontend/env_example](/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/frontend/env_example.md)
- [x] 4.2) Import the router in the `main.js` (or `main.ts`) file: [/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/frontend/src/main.js](/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/frontend/src/main.js)
- [x] 4.3) Create the router-config file and setup its options: [/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/frontend/src/router/index](/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/frontend/src/router/index.md)
- [x] 4.4) (Optional) Make sure you already have all views ("pages") as `.vue` files organized in `/frontend/src/views/` folders. Don't develop those views now. Just create them!
- [x] 4.5) In `/frontend/src/App.vue`, define where views ("pages") must be rendered, adding `<RouterView />` in the `<template>` layer of the SFC: [/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/frontend/src/App.vue](/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/frontend/src/App.vue)).
- [x] 4.6) Define each link option (`<RouterLink>`) for the app's main menu: [/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/frontend/src/components/navigation/MainMenu](/javascript/web-development/frontend/vue/component-libraries/vue-router/example-SPA/frontend/src/components/navigation/MainMenu.md)

---
## 5) (If applicable / Optional) Testing:
If you got the front-end entirely configured with all its dependencies installed and integrated, you can test it:
[/javascript/web-development/frontend/vue/vue-knowledge/\_running-app](/javascript/web-development/frontend/vue/vue-knowledge/_running-app.md)
Otherwise, it's better to finish all front-end dependencies first!


        
                
