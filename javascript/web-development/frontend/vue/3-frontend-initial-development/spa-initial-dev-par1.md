#### JavaScript > Front-end > Vue
# Initial development roadmap for SPA [Part 1/2]

---
## Before:
- This roadmap is part of the initial development roadmap: [/javascript/web-development/frontend/vue/3-frontend-initial-development/\_initial-roadmap](/javascript/web-development/frontend/vue/3-frontend-initial-development/_initial-roadmap.md)
- What's SPA: [/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture](/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture.md)

---
## 1) Basic structure and navigation:
- [x] 1.1) Based on the sitemap, and don't waste time on design, just create every view (page) as a SFC (`.vue`): [/javascript/web-development/frontend/vue/3-frontend-initial-development/creating-sfc](/javascript/web-development/frontend/vue/3-frontend-initial-development/creating-sfc.md)
- [x] 1.2) Navigation components - create every planned menu in `/frontend/src/components/navigation/`. Don't waste time coding now. Just create them with placeholders.

---
## 2) Layout and routing architecture:
- [ ] 2.1) Implement `PublicLayout.vue` and `LoggedLayout.vue`. Small or simple product solution don't need more than one layout most cases.
- [ ] 2.2) Vue Router: based on the app's sitemap document:
	- Refactor your `/frontend/src/router/index.ts` (or `.js`) as needed: [/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/spa/project_root_using_ts/frontend/src/router/index.ts](/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/spa/project_root_using_ts/frontend/src/router/index.ts).
	- (If applicable) Only for TypeScript projects, declare the types you are using in router: [/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/spa/project_root_using_ts/frontend/src/types/vue-router.d.ts](/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/spa/project_root_using_ts/frontend/src/types/vue-router.d.ts)
- [ ] 2.3) Configure authentication route guards (initially using a simulator): [/javascript/web-development/frontend/vue/3-frontend-initial-development/authentication-simulator](/javascript/web-development/frontend/vue/3-frontend-initial-development/authentication-simulator.md)

Done.

---
## Return to main initial development roadmap:
 [/javascript/web-development/frontend/vue/3-frontend-initial-development/\_initial-roadmap](/javascript/web-development/frontend/vue/3-frontend-initial-development/_initial-roadmap.md)


