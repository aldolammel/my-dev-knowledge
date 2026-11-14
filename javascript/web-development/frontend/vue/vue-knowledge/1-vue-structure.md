#### JavaScript > Vue > Structure
# Files & Folder Structure

---

==IMPORTANT==: 
If you are using Vite as Built-tool, it already will manage the `.scss` files compilation as well as other files compilation. So try do NOT customize compilation paths, like to force the `.css` files in `/public/` folder!

More about compilation time: [/javascript/web-development/frontend/vue/vue-knowledge/90-go-live-compilation](/javascript/web-development/frontend/vue/vue-knowledge/90-go-live-compilation.md)

---
## Vue folder structure:
For TypeScript, most of the `.js` files will be `.ts`. In the right moment of the Vue installation roadmaps, when it's asked, you can take file examples to your `/frontend/src/` from:
[/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/project_root/frontend/src/](/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/project_root/frontend/src/) (folder)
```python
my_project/
├── frontend/
│   ├── node_modules/        # stores all dependencies of the project and node.js stuff.
│   │
│   ├── public/              # Use it for static assets you reference by absolute path.
│   │   ├── favicon.ico
│   │   ├── manifest.json    # for PWA configuration.
│   │   ├── robots.txt       # xxxxx.
│   │   ├── sitemap.xml      # xxxxx.
│   │   └── ...
│   │
│   ├── src/                   # Where Vue project is. Vite build-tool watches this folder!
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
│   │   │   └── ...
│   │   │
│   │   ├── components/
│   │   │   ├── common/               # Reusable dumb components (Button, Modal).
│   │   │   │   ├── BestProducts.vue  
│   │   │   │   ├── Newsletter.vue       
│   │   │   │   ├── Testimonials.vue  
│   │   │   │   └── ...
│   │   │   │
│   │   │   ├── layout/               # Layout components (AppHeader, Navigation).
│   │   │   │   ├── SiteHeader.vue
│   │   │   │   ├── SiteFooter.vue
│   │   │   │   ├── NavMain.vue
│   │   │   │   └── ...
│   │   │   │
│   │   │   └── pages/                # Components specific to a page/route.
│   │   │       ├── Home.vue
│   │   │       ├── ListByCategory.vue
│   │   │       ├── LoadBlog.vue
│   │   │       ├── LoadBlogPost.vue
│   │   │       └── ...
│   │   │
│   │   ├── composables/              # Reusable functions for Composition API.
│   │   │   ├── useErrorHandler.js
│   │   │   ├── usePage.js
│   │   │   └── ...
│   │   │
│   │   ├── hooks/                # For custom Composition API functions (hooks).
│   │   │   ├── useAuth.js
│   │   │   └── ...
│   │   │
│   │   ├── libs/                 # Where all main library files are. Things connected to the world.
│   │   │   ├── bootstrap.js
│   │   │   └── ...
│   │   │
│   │   ├── router/           # Where routes and lazy-load pages are defined.
│   │   │   ├── router.js     # Router config file.
│   │   │   └── routes.js     # Where routes are defined.
│   │   │
│   │   ├── stores/           # Where things are caching from APIs.
│   │   │   ├── menus.js      # Caching/storing data from menus managed by back-end.
│   │   │   └── pages.js      # Caching/storing data from pages managed by back-end.
│   │   │
│   │   ├── utils/            # Tiny, pure funcs that do one thing, but not lib or Vue reactivity.
│   │   │   ├── env.js        # Calling front-end environment vars.
│   │   │   └── tinyslider-testimonial.js
│   │   │
│   │   ├── App.vue           # Root component page (main-vue-app).  <---------------
│   │   └── main.js           # Vue app init.
│   │
│   ├── .env                  # Exclusive front-end environment variables. 
│   ├── index.html            # Run it to see the app on the browser. 
│   └── package.json
│
├── .nvmrc                    # File used to load the correct project Node version!
└── ...
```

---
## Back-end framework structures working with Vue:
- Django folder project with Vue: [/javascript/web-development/frontend/vue/1-install-and-first-steps/project-folder-structure-vue-and-django](/javascript/web-development/frontend/vue/1-install-and-first-steps/project-folder-structure-vue-and-django.md)

---
## A Vue app file (`.vue`) is divided by 3 layers:
1) `<script>`
2) `<template>`
3) `<style>`
### `<script>` layer
There are 2-ways to code components, using 'Options API' or 'Component API' but both use JavaScript (TypeScript is optional) to be written:
- [/javascript/web-development/frontend/vue/vue-knowledge/3-approaches-to-code](/javascript/web-development/frontend/vue/vue-knowledge/3-approaches-to-code.md)
### `<template>` layer
Templates is basically pure HTML, and each template can be fragmented in infinite other small pieces, using Vue Component structure associated with Vue Slots:   
- [/javascript/web-development/frontend/vue/vue-knowledge/5-components](/javascript/web-development/frontend/vue/vue-knowledge/5-components.md)
- [/javascript/web-development/frontend/vue/vue-knowledge/5.4-slot](/javascript/web-development/frontend/vue/vue-knowledge/5.4-slot.md)
### `<style>` layer
Each component (.vue file, for example) can have its own `<style>` tag where all the style coded in there can be global (for the parent component and its child ones) or local so the style tag is restricted only to the component the style tag belongs.
```js
<!-- if 'scoped', the style is only local for the current component -->
<style scoped>
...
</style>
```

---
## MORE ABOUT:
[/javascript/web-development/frontend/vue/vue-knowledge/0-overview-deep-knowledge](/javascript/web-development/frontend/vue/vue-knowledge/0-overview-deep-knowledge.md)
## INSTALL A VUE PROJECT:
[/javascript/web-development/frontend/vue/1-install-and-first-steps/0-vue-installation-and-setup](/javascript/web-development/frontend/vue/1-install-and-first-steps/0-vue-installation-and-setup.md)






