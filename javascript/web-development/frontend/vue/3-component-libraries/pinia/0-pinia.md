#### JavaScript > Vue > Components & Libraries
# Pinia

---

==It replaces Vuex needs in Vue 3==

Pinia is a (global) state management library designed specifically for Vue 3. It offers a lightweight and intuitive approach to app state management. It allows devs to create and organize stores by encapsulating state and app logic in a centralized module. Additionally, it enables us to share the state between elements and pages (components and views), creating a user-friendly experience using the new responsive concept in Vue3. Not all apps need access to a global state, but if yours need one, Pinia will make it easier.

https://pinia.vuejs.org/

**What is a store?**

A store is an entity holding state and business logic that isn't bound to your Component tree. In other words, it hosts global state. It's a bit like a component that is always there and that everybody can read off and write to. It has three concepts, the state, getters and actions and it's safe to assume these concepts are the equivalent of data, computed and methods in components.

**Pinia VS Vuex:**
- Encourages multiple stores (that can easily communicate) instead of a single global store;
- No mutations once state can be modified directly;
- It's much easier to import stores into any component or composable;
- Better (default) TypeScript support;
- Native support for Vue DevTools;
- Extremely lightweight: around 1.5kb.

**When Pinia isn't necessary:**
- Simple state management:
	- For a few bunch of pages you can manage state using Vue's built-in ref(), reactive(), and provide/inject APIs.
- Django as single source of truth:
	- Since you're using Django back-end, most persistent data should come from your Django API endpoints.
- Minimal client-side complexity:
	- Institutional websites typically have straightforward data flows without complex inter-component state sharing.

**Consider Pinia if you have:**
- Cross-page state persistence (user preferences, shopping cart-like features);
- Complex component hierarchies sharing the same data;
- Real-time features requiring centralized state updates;
- Client-side caching needs for API responses.

Data-flow of a real Vue Pinia usage: [/python/web-development/django/useful-sub-apps/pagex/docs/django-with-vue-integration.excalidraw](/python/web-development/django/useful-sub-apps/pagex/docs/django-with-vue-integration.excalidraw)

---
## 1) Which Vue build-tool are you using?

- 1A) Using Vue-CLI.
- 1B) Using Vue-Vite (Recommended). 

......................................

### 1A) Using Vue-CLI
Pinia team's recommending this unofficial plugin (2025): https://github.com/wobsoriano/vue-cli-plugin-pinia
More about: https://pinia.vuejs.org/getting-started.html

......................................

### 1B) Using Vue-Vite

Installing Pinia:

Before:
- Assuming you are in the `/frontend/` folder.

To install:
```bash
npm install pinia
```
Check it:
```bash
npm list
```
To uninstall:
```bash
npm uninstall pinia
```

---
## 2) Integration:
[/javascript/web-development/frontend/vue/3-component-libraries/pinia/1-overview-how-to-create-data](/javascript/web-development/frontend/vue/3-component-libraries/pinia/1-overview-how-to-create-data.md)

---
## For Vue 2 projects, use Vuex:
[/javascript/web-development/frontend/vue/3-component-libraries/vuex/0-vuex](/javascript/web-development/frontend/vue/3-component-libraries/vuex/0-vuex.md)




