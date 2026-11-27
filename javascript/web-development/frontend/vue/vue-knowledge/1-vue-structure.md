#### JavaScript > Vue > Structure
# Files & Folder Structure

---

==IMPORTANT ABOUT CSS==: 
If you are using Vite as built-tool, it will manage the `.scss` files compilation as well as other files compilation. So try do NOT customize compilation paths, like to force the `.css` files in `/public/` folder! More about compilation time: [/javascript/web-development/frontend/vue/vue-knowledge/90-go-live-compilation](/javascript/web-development/frontend/vue/vue-knowledge/90-go-live-compilation.md)

---

==DON'T CREATE FOLDERS BEFORE BUILD-TOOL INSTALL==
When a Vue roadmap explicit asks you to copy folders and files, you should take them from here:
- For **SPA**:
	- Using `.js`: `/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/spa/project_root_using_js/`
	- Using `.ts`: `/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/spa/project_root_using_ts/`
- For **MPA**:
	- Using `.js`: `/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/mpa/project_root_using_js/`
	- Using `.ts`: `/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/mpa/project_root_using_ts/`
- Additional attention for **STATIC** project: you don't need [these files and folders](/javascript/web-development/frontend/vue/vue-knowledge/static-project-file-structure.md).

---
## Vue folder structure for SPA architecture
If the project is defined to use TypeScript, most of `.js` files must be considered as `.ts`:
```python
my_project/
├── frontend/
│   ├── node_modules/        # stores all dependencies of the project and node.js stuff.
│   │
│   ├── public/              # Use it for static assets you reference by absolute path.
│   │   ├── favicon.ico
│   │   ├── manifest.json    # for PWA configuration, if functionality implemented.
│   │   ├── robots.txt       # xxxxx.
│   │   ├── sitemap.xml      # xxxxx.
│   │   └── ...
│   │
│   ├── src/                   # Where Vue project is. Vite build-tool watches this folder!
│   │   ├── api/               # Axios layer. Views/stores never call Axios directly.
│   │   │   ├── http.ts        # Axios instance (baseURL, interceptors, CSRF/token).
│   │   │   ├── auth.api.ts
│   │   │   └── ...
│   │   │
│   │   ├── assets/            # Those files that aren't public.
│   │   │   ├── imgs/          # Images that need optimization or processing.
│   │   │   │   ├── logo.svg
│   │   │   │   ├── bg.jpg
│   │   │   │   └── ...
│   │   │   │
│   │   │   ├── styles/                  # Files to imported in components or main.js.
│   │   │   │   ├── app.scss             # Everything about this project product styling.
│   │   │   │   ├── css-framework.scss   # It imports CSS framework installed.
│   │   │   │   └── ...
│   │   │   │
│   │   │   ├── icons/
│   │   │   │   └── ...
│   │   │   │
│   │   │   └── ...
│   │   │
│   │   ├── components/                        # Reusable, NON-routed SFCs.
│   │   │   ├── common/                        # Generic blocks to be used in views (pages).
│   │   │   │   ├── NewsletterFormCommon.vue
│   │   │   │   └── ...
│   │   │   │
│   │   │   ├── navigation/                  
│   │   │   │   ├── MainMenu.vue  
│   │   │   │   ├── FooterMenu.vue       
│   │   │   │   ├── LangSwitcher.vue
│   │   │   │   └── ...
│   │   │   │
│   │   │   └── ...
│   │   │
│   │   ├── composables/              # Reusable functions for Composition API.
│   │   │   ├── useAuth.ts            # Reads /stores/auth.ts and exposes auth status and permission helpers to the front-end.
│   │   │   ├── useErrorHandler.ts
│   │   │   └── ...
│   │   │
│   │   ├── layouts/                  # Shells that wrap routed views via <RouterView />.
│   │   │   ├── PublicLayout.vue
│   │   │   ├── LoggedLayout.vue
│   │   │   └── ...
│   │   │
│   │   ├── libs/                 # Where main library files are. Things connected to the world.
│   │   │   ├── bootstrap.ts
│   │   │   ├── i18n.ts
│   │   │   └── ...
│   │   │
│   │   ├── locales/              # Translations for multiligual projects.
│   │   │   ├── en.json
│   │   │   ├── pt-BR.json
│   │   │   └── ...
│   │   │
│   │   ├── router/           # NOT used in MPA.
│   │   │   ├── index.ts      # Router config + lazy-loaded views.
│   │   │   ├── routes.ts     # Route definitions (public / authenticated / system).
│   │   │   └── guards.ts     # Controls route access and redirects based on auth status from useAuth.ts.
│   │   │
│   │   ├── stores/           # Pinia: where things are caching from APIs.
│   │   │   ├── auth.ts       # Holds reactive auth state and actions where Pinia stores user authentication data.
│   │   │   └── ...
│   │   │
│   │   ├── types/            # Only in case using TypeScript: TS definitions
│   │   │   └── ...
│   │   │
│   │   ├── utils/            # Tiny, pure funcs that do one thing, but not lib or Vue reactivity.
│   │   │   ├── env.ts        # Calling front-end environment vars.
│   │   │   └── ...
│   │   │
│   │   ├── views/                   # In Vue, 'views' means 'pages'. One file per route.
│   │   │   ├── public/              # Views available for everyone (visitors).
│   │   │   │   ├── HomeView.vue
│   │   │   │   ├── LoginView.vue
│   │   │   │   ├── RegisterView.vue
│   │   │   │   ├── AboutView.vue
│   │   │   │   ├── TermsView.vue
│   │   │   │   └── ...
│   │   │   │
│   │   │   ├── logged/               # Views available only for authenticated users.
│   │   │   │   ├── HomeView.vue
│   │   │   │   └── ...
│   │   │   │
│   │   │   └── sys/
│   │   │       ├── PwdForgottenView.vue
│   │   │       ├── EmailConfirmedView.vue
│   │   │       ├── ForbiddenView.vue            # Error 403
│   │   │       ├── NotFoundView.vue             # Error 404
│   │   │       └── ...
│   │   │
│   │   ├── App.vue           # Root component: just <RouterView />.  <---------------
│   │   └── main.ts           # Single Vue app init (Pinia, router, i18n).
│   │
│   ├── .env                  # Exclusive front-end environment variables. 
│   ├── index.html            # Run it to see the app on the browser. 
│   └── package.json          # Collection of front-end dependencies.
│
├── .nvmrc                    # File used to load the right project's Node version.
└── ...
```

---
## Vue folder structure for MPA architecture
If the project is defined to use TypeScript, most of `.js` files must be considered as `.ts`:
```python
my_project/
├── frontend/
│   ├── node_modules/
│   │
│   ├── public/
│   │   ├── favicon.ico
│   │   ├── manifest.json 
│   │   ├── robots.txt
│   │   ├── sitemap.xml
│   │   └── ...
│   │
│   ├── src/
│   │   ├── api/
│   │   │   ├── http.ts
│   │   │   ├── auth.api.ts
│   │   │   └── ...
│   │   │
│   │   ├── assets/
│   │   │   ├── imgs/
│   │   │   │   ├── logo.svg
│   │   │   │   ├── bg.jpg
│   │   │   │   └── ...
│   │   │   │
│   │   │   ├── styles/
│   │   │   │   ├── app.scss
│   │   │   │   ├── css-framework.scss
│   │   │   │   └── ...
│   │   │   │
│   │   │   ├── icons/
│   │   │   │   └── ...
│   │   │   │
│   │   │   └── ...
│   │   │
│   │   ├── components/
│   │   │   ├── common/
│   │   │   │   ├── NewsletterFormCommon.vue
│   │   │   │   └── ...
│   │   │   │
│   │   │   ├── navigation/                  
│   │   │   │   ├── MainMenu.vue  
│   │   │   │   ├── FooterMenu.vue       
│   │   │   │   ├── LangSwitcher.vue
│   │   │   │   └── ...
│   │   │   │
│   │   │   └── ...
│   │   │
│   │   ├── composables/
│   │   │   ├── useAuth.ts
│   │   │   └── ...
│   │   │
│   │   ├── guards/                       # For MPA, it replaces router guards: called by each page entry.
│   │   │   ├── requireAuth.ts            # Redirects visitors to login.html.
│   │   │   └── requireGuest.ts           # Redirects authenticated users away from login and registration.
│   │   │
│   │   ├── layouts/
│   │   │   ├── PublicLayout.vue
│   │   │   ├── LoggedLayout.vue
│   │   │   └── ...
│   │   │
│   │   ├── libs/
│   │   │   ├── createPageApp.ts          # Shared bootstrap: createApp + Pinia + i18n.
│   │   │   ├── bootstrap.ts
│   │   │   ├── i18n.ts
│   │   │   └── ...
│   │   │
│   │   ├── locales/
│   │   │   ├── en.json
│   │   │   ├── pt-BR.json
│   │   │   └── ...
│   │   │
│   │   ├── pages/                        # Replaces views/ and router/: one folder per HTML entry.
│   │   │   ├── home/
│   │   │   │   ├── main.ts               # Calls createPageApp(HomePage).
│   │   │   │   └── HomePage.vue
│   │   │   │
│   │   │   ├── login/
│   │   │   │   ├── main.ts
│   │   │   │   └── LoginPage.vue
│   │   │   │
│   │   │   ├── about/
│   │   │   │   ├── main.ts
│   │   │   │   └── AboutPage.vue
│   │   │   │
│   │   │   ├── terms/
│   │   │   │   ├── main.ts
│   │   │   │   └── TermsPage.vue
│   │   │   │
│   │   │   └── ...
│   │   │
│   │   ├── stores/          # Pinia: state DOESN'T survive pg loads, so persist what matters in storage/cookies.
│   │   │   ├── auth.ts
│   │   │   └── ...
│   │   │
│   │   ├── types/
│   │   │   └── ...
│   │   │
│   │   └── utils/
│   │       ├── env.ts
│   │       └── ...
│   │
│   ├── index.html                   # One HTML entry per page.
│   ├── login.html                   # If using Vite, vite.config.ts > build.rollupOptions.input.
│   ├── register.html                # One HTML entry per page.
│   ├── about.html                   # One HTML entry per page.
│   ├── terms.html                   # One HTML entry per page.
│   ├── ...
│   │
│   ├── .env
│   ├── vite.config.ts               # If using Vite, lists every .html in build.rollupOptions.input.
│   ├── package.json
│   └── ...
│
├── .nvmrc
└── ...
```

---
## Back-end framework structures working with Vue:
- For Django project with Vue: [/javascript/web-development/frontend/vue/1-install-and-first-steps/project-folder-structure-vue-and-django](/javascript/web-development/frontend/vue/1-install-and-first-steps/project-folder-structure-vue-and-django.md)

---
## A Vue app file, best known as SFC (`.vue`):
Every Single-File-Component (SFC) is divided by 3 layers:
1) **`<script>`**
	- There are 2-ways to code components: using *Options API* or *Component API*, but both use JavaScript (TypeScript is optional) to be written:
		- [/javascript/web-development/frontend/vue/3-frontend-initial-development/component-approaches](/javascript/web-development/frontend/vue/3-frontend-initial-development/component-approaches.md)
2) **`<template>`**
	- Templates tag is basically pure HTML, and each template can be fragmented in infinite other small pieces, using Vue Component structure associated with Vue Slots:
		- [/javascript/web-development/frontend/vue/vue-knowledge/5-components](/javascript/web-development/frontend/vue/vue-knowledge/5-components.md)
		- [/javascript/web-development/frontend/vue/vue-knowledge/5.4-slot](/javascript/web-development/frontend/vue/vue-knowledge/5.4-slot.md)
3) **`<style>`**
	- Every SFC (`.vue` file) can have its own `<style>` tag where all its style coded can be global (for the parent component and its child ones) or local so the style tag is restricted only to the component the style tag belongs.
```vue
<!-- if 'scoped', the style is only local for the current component -->
<style scoped>
...
</style>

<!-- if no scopted used, the style will be global for all component children of this SFC, including its parent -->
<style>
...
</style>
```

---
## More about Vue:
[/javascript/web-development/frontend/vue/vue-knowledge/0-overview-deep-knowledge](/javascript/web-development/frontend/vue/vue-knowledge/0-overview-deep-knowledge.md)
## Installing a Vue project from the scratch:
[/javascript/web-development/frontend/vue/1-install-and-first-steps/0-vue-installation-and-setup](/javascript/web-development/frontend/vue/1-install-and-first-steps/0-vue-installation-and-setup.md)






