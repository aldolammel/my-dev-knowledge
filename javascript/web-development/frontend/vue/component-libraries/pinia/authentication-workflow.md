#### JavaScript > Front-end > Vue > Components & Libraries > Pinia
# Pinia: authentication work-flow

---
## In [SPA](/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture.md) architecture:

1. **`/stores/auth.ts`:** 
	- Holds reactive auth state and actions where Pinia stores user authentication data.
2. **`/composables/useAuth.ts`:** 
	- Reads `auth.ts` and exposes auth status and permission helpers to the front-end. Basically it's what you import to views, components, and layouts!
3. **`/router/guards.ts`:**
	- Controls route access and redirects based on auth status from `useAuth.ts`.

---
## In [MPA](/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture.md) architecture:
Soon...

---
## Creating a fake authentication solution before implement Pinia:
[/javascript/web-development/frontend/vue/component-libraries/pinia/fake-authentication](/javascript/web-development/frontend/vue/component-libraries/pinia/fake-authentication)



