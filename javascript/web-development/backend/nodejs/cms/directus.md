

---

Directus is an open-source, Node.js-based headless [CMS](/dev-concepts/cms.md) and [BaaS](/dev-concepts/BaaS.md) that acts as an [API](/api/_about.md) and no-code data studio layer on top of any new or existing SQL database.

---
## Core Architecture:
- **Database Mirroring (Zero Lock-In):** Unlike CMS platforms that force your content into proprietary schemas, Directus inspects your SQL database (PostgreSQL, MySQL, SQLite, MS SQL, MariaDB, Oracle, CockroachDB) in real time and mirrors it. You retain pure SQL access and full data ownership.
- **Instant APIs:** It dynamically generates REST and GraphQL endpoints, plus a WebSockets interface for real-time updates, directly from your database schema.
- **Tech Stack:** Built on Node.js for the back-end engine and [Vue.js](/javascript/web-development/frontend/vue/_about.md) for the customizable, white-label admin web app ("Data Studio").


https://directus.com/