#### JavaScript > Vue > Components & Libraries
# Vue Router: installation and integration

---

==If you are using Vue-CLI==
If you already created your project via Vue-CLI (default), you probably already have the Router once it was an Vue-CLI option during the project creation process. Make sure about checking it through the Vue project folder:
```bash
npm list
```
If you don't see any router stuff, keep with the installation and integration processes below, otherwise skip this roadmap!

---
## 1) Installing:
To install Vue-Router:
```bash
npm install vue-router@<version you want>
# E.g. npm install vue-router@latest
```

Check installation:
```bash
npm list vue-router
```

Uninstall (if needed): [/javascript/web-development/frontend/vue/3-component-libraries/vue-router/router-uninstall](/javascript/web-development/frontend/vue/3-component-libraries/vue-router/router-uninstall.md)

---
## 2) Integration:
- SPA) For Single-Page-Application (SPA).
- MPA) Or for Multi-Pages-Application (MPA).

......................................

### SPA) For SPA project

SPA.1) In the `/frontend/.env` file, create these env vars: [/javascript/web-development/frontend/vue/3-component-libraries/vue-router/example-SPA/project_one/frontend/env_example](/javascript/web-development/frontend/vue/3-component-libraries/vue-router/example-SPA/project_one/frontend/env_example.md)

SPA.2) Import the router and setup the very basic in the `main.js` file: [/javascript/web-development/frontend/vue/3-component-libraries/vue-router/example-SPA/project_one/frontend/src/main.js](/javascript/web-development/frontend/vue/3-component-libraries/vue-router/example-SPA/project_one/frontend/src/main.js)

SPA.3) Create the router-config file and setup its options: [/javascript/web-development/frontend/vue/3-component-libraries/vue-router/example-SPA/project_one/frontend/src/router/index.js](/javascript/web-development/frontend/vue/3-component-libraries/vue-router/example-SPA/project_one/frontend/src/router/index.js)

SPA.4) Make sure you already have all views ("pages") in the `/frontend/src/pages/` folder. E.g.:
- Home.vue
- About.vue
- Contact.vue

SPA.5) Define where all views ("pages") must be rendered in your front-end template:
Add this where each View must be loaded: `<RouterView />`
E.g.: [/javascript/web-development/frontend/vue/3-component-libraries/vue-router/example-SPA/project_one/frontend/src/App.vue](/javascript/web-development/frontend/vue/3-component-libraries/vue-router/example-SPA/project_one/frontend/src/App.vue)

SPA.6) Define each link option (`<RouterLink>`) for the main navigation menu of the app. E.g.: [/javascript/web-development/frontend/vue/3-component-libraries/vue-router/example-SPA/project_one/frontend/src/components/NavMain.vue](/javascript/web-development/frontend/vue/3-component-libraries/vue-router/example-SPA/project_one/frontend/src/components/NavMain.vue)

......................................
            
### MPA) For MPA project

            <MPA needs ROUTER ????????????????????????????????>

            MPA.1) xxxxxxxxxxxxxxxxxxxx

            MPA.2) xxxxxxxxxxxxxxxxxxxx

            MPA.3) xxxxxxxxxxxxxxxxxxxx

            MPA.4) xxxxxxxxxxxxxxxxxxxx

            MPA.5) xxxxxxxxxxxxxxxxxxxx

---
## 3) Testing:
[/javascript/web-development/frontend/vue/vue-knowledge/\_running-app](/javascript/web-development/frontend/vue/vue-knowledge/_running-app.md)


        
                
