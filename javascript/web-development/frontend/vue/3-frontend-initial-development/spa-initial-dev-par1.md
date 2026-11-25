#### JavaScript > Front-end > Vue
# Initial development roadmap for SPA [Part 1/2]

---
## Before:
- This roadmap is part of the initial development roadmap: [/javascript/web-development/frontend/vue/3-frontend-initial-development/\_initial-roadmap](/javascript/web-development/frontend/vue/3-frontend-initial-development/_initial-roadmap.md)
- What's SPA: [/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture](/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture.md)

---
## 1) Basic structure and navigation:
- [x] 1.1) Based on the sitemap, and don't wasting your time with design, just create every view (page) as a SFC (`.vue`) file, respecting what is view/public and what is view/logged.
- [x] 1.2) Navigation components - create every planned menu in `/frontend/src/components/navigation/`. Don't waste time coding now. Just create them with placeholders.

---
## 2) Layout and routing architecture:
- [x] 2.1) Implement `PublicLayout.vue` and `LoggedLayout.vue`. Small or simple product solution don't need more than one layout most cases.
- [x] 2.2) Vue Router: refactor  `/frontend/src/router/index.ts` (or `.js`) to use nested routes and to include layouts (`/src/layouts/`), adding every view (page) from the sitemap document you've defined with their paths. [Example](/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/spa/project_root_using_ts/frontend/src/router/index.ts).
- [x] 2.3) Make sure you are keeping the system views (`/src/views/sys/`) outside the public and authenticated layouts.
- [x] 2.4) Configure authentication route guards (initially using a simulator): [/javascript/web-development/frontend/vue/3-frontend-initial-development/authentication-simulator](/javascript/web-development/frontend/vue/3-frontend-initial-development/authentication-simulator.md)

Done.

---
## Return to main initial development roadmap:
 [/javascript/web-development/frontend/vue/3-frontend-initial-development/\_initial-roadmap](/javascript/web-development/frontend/vue/3-frontend-initial-development/_initial-roadmap.md)


