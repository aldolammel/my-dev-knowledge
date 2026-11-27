#### JavaScript > Vue > Structure
# Files & Folder Structure (only for STATIC products)

---
## 1) Keep using what is saying there:
[/javascript/web-development/frontend/vue/vue-knowledge/1-vue-structure](/javascript/web-development/frontend/vue/vue-knowledge/1-vue-structure.md)

But you definitely DON'T need these files below, according your application architecture.

---
## To exclude from Static SPA projects:

| Don't                   | Why                                                             |
| ----------------------- | --------------------------------------------------------------- |
| `/api/`<br>             | ...                                                             |
| `/router/guards.ts`<br> | Determines who can and cannot access areas of the application.  |
| `/stores/`              | Where the dynamic content is stored.                            |
| `/views/logged/`        | Only views where the content is focused to authenticated users. |
| ...                     | ...                                                             |
| ...                     | ...                                                             |

---
## To exclude from Static MPA projects:

| Don't         | Why                                                            |
| ------------- | -------------------------------------------------------------- |
| `/api/`<br>   | ...                                                            |
| `/guards/*.*` | Determines who can and cannot access areas of the application. |
| ...           | ...                                                            |
| ...           | ...                                                            |

---



