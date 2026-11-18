#### Dev concepts > Web development
# Application architecture

---

In web development, app architecture defines how an application generates, delivers, and manages its content and how its front-end communicates with the back-end. An critical distinction to do is a web project can be more than one application architecture concept.

---
### Static Site Generation (SSG)
Generates HTML pages at build time.

Some technologies that support this architecture:
- [VitePress](/javascript/build-tools/vite/vitepress.md)
- [Flask](/python/web-development/flask/_about.md)

..........

### Single-Page Application (SPA)
Loads one main HTML document and handles navigation in the browser. Closely related to the CSR, the difference is the SPA describes how the app handles navigation (typically without reloading the HTML).

Some technologies that support this architecture:
- [Angular](/javascript/web-development/frontend/angular/angular-knowledge/_about.md)
- [React](/javascript/web-development/frontend/react/react-knowledge/_about.md)
- [Vue.js](/javascript/web-development/frontend/vue/vue-knowledge/_about.md)

..........

### Multi-Page Application (MPA)
Each navigation typically requests a new HTML document from the server.

Some technologies that support this architecture:
- [Django](/python/web-development/django/_about.md) (Django Templates + HTML/CSS/JS).
- [Flask](/python/web-development/flask/_about.md) (Jinja2 + HTML/CSS/JS).
- [Vue.js](/javascript/web-development/frontend/vue/vue-knowledge/_about.md) (each page has its own HTML, and Vue doesn't necessarily manage routing).

..........

### Server-Side Rendering (SSR)
Each navigation typically requests a new HTML document from the server. For example, one crucial difference between SSR and CSR is their rendering strategies.

Some technologies that support this architecture:
- [Django](/python/web-development/django/_about.md)
- Next.js
- [Nuxt.js](/javascript/web-development/frontend/vue/3-component-libraries/nuxt/_about.md)

..........

### Client-Side Rendering (CSR)
Each navigation typically requests a new HTML document from the server. Closely related to the SPA, the difference is the CSR describes where the HTML interface is rendered (in the browser using JS). Another important thing, but about CSR and SSR is their rendering strategies.

Some technologies that support this architecture:
- [Django](/python/web-development/django/_about.md) (Django REST API)
- [Flask](/python/web-development/flask/_about.md)
- [FastAPI](/python/web-development/fast-api/_about.md)
- [Angular](/javascript/web-development/frontend/angular/angular-knowledge/_about.md)
- [React](/javascript/web-development/frontend/react/react-knowledge/_about.md)
- [Vue.js](/javascript/web-development/frontend/vue/vue-knowledge/_about.md)

..........

### And others
- Incremental Static Regeneration (ISR):
- Deferred Static Generation (DSG):

---
## Practical examples:

- SSG + MPA: Static website with traditional page navigation (e.g., fastest webpage someone can create).
- SSR + MPA: Traditional Back-end-rendered website (e.g. most common Django project).
- CSR + SPA: Vue application communicating with a Django REST API.
- SSR + SPA: Server-rendered initial HTML followed by client-side navigation (hydration).