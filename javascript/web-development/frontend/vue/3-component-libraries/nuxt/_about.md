#### JavaScript > Vue
# Nuxt.js

---

Nuxt is a free, open-source, full-stack web framework built on top of [Vue.js](/javascript/web-development/frontend/vue/vue-knowledge/_about.md). It simplifies web development by combining Vue for the user interface with [Vite](/javascript/build-tools/vite/_install.md) for building assets and Nitro as a server engine.

|                             | **Vue 3** (with Vite)                            | **Nuxt** (Vite incorporated)                                                                 |
| --------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| SEO & Public Content        | Poor (renders via JS in browser)                 | Best (SSR & SSG pre-render HTML)                                                             |
| Dashboards / Internal Tools | Best (simpler, zero server overhead)             | Overkill unless you want the structure                                                       |
| Backend / API Routes        | Requires separate backend (e.g., Python/FastAPI) | **Built-in** ([Nitro](javascript/web-development/backend/nodejs/component-libraries/nitro/_about.md) server engine) |
| Setup & Routing             | Manual (`vue-router`, Pinia, imports)            | **Zero-config** (file-based routing, auto-imports)                                           |
| Hosting                     | Cheap/free static hosting anywhere               | Needs Node/Edge runtime (unless using SSG)                                                   |

---
## Install:
[/javascript/web-development/frontend/vue/3-component-libraries/nuxt/\_install](/javascript/web-development/frontend/vue/3-component-libraries/nuxt/_install.md)




