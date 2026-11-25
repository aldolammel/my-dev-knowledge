#### JavaScript > Front-end > Vue > Project types
# Vue-only project solution, but still dynamic

---

Vue is only a front-end framework that runs over Node.js. Actually, Node can store data in `.json` files (using modules) or also create connections to a database (like PostgreSQL, MariaDB, SQLite, etc). So it can be a flawless solution for small web products.

---
## Before:
- If you need a static solution, without db and CMS, but still using Vue benefits, skip to: [/javascript/web-development/frontend/vue/0-new-project/web-project-static-vue-only](/javascript/web-development/frontend/vue/0-new-project/web-project-static-vue-only.md)

---
## 1) Define the needs:
- 1A) Dynamic Vue-only solution with a file-based content management (RECOMMENDED).
- 1B) Dynamic Vue-only solution with a real but simple content management ability.

......................................

### 1A) Dynamic Vue-only solution with a file-based content management
Since Node has built-in file system capabilities (`fs`), you can store your content directly in `.json` files or Markdown (`.md`) files inside your project folder.

Soon...

......................................

### 1B) Dynamic Vue-only solution with a real but simple content management ability
If you want a visual CMS where you can log in and type content without editing raw code or files, you can use a *Headless CMS* built on Node.

==TO THINK==
If you're considering to use CMS in a Vue project, but JavaScript is not a mandatory language for the entire solution, consider a server-side CPU/RAM lighter consumer option:
- Lightest - [using Python + FastAPI + Moosey CMS + Vue](/python/web-development/fast-api/0-new-project/web-project-fastapi-with-vue.md): no db needed, it's a flat-file `.md` CMS, eliminating memory and CPU overhead!
- Lighter - [using Python + Flask + FlaskAdmin CMS + Vue](/python/web-development/flask/0-new-project/web-project-flask-with-vue.md): requires a db but still much lighter than Node.js solution.

That said, if JS still what you need, let's go:

**Lighter Node CMS:**
- [Directus](/javascript/web-development/backend/nodejs/cms/directus.md)

**Not great solution:**
- [Payload](/javascript/web-development/backend/nodejs/cms/payload.md) - poor Vue support.
- [Strapi](/javascript/web-development/backend/nodejs/cms/strapi.md) - relative high RAM consumer for what you need here!

---

