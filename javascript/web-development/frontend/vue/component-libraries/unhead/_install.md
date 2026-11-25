#### JavaScript > Front-end > Vue > Components & Libraries
# Unhead-Vue

---

Unhead-Vue is a Vue 3 integration library for Unhead, which is a [framework-agnostic](/dev-concepts/agnostic.md) library for managing the `<head>` of your HTML document. So Unhead-Vue allows you to dynamically and programmatically manage your document's `<head>` section (metadata, SEO tags) in Vue 3 apps.

**Key Features:**
- Update document title dynamically;
- Manage meta tags (description, keywords, Open Graph, Twitter Cards, etc);
- Control link tags (canonical, stylesheets, preload, prefetch);
- Handle script tags and JSON-LD structured data;
- Manage viewport and other head elements.

**For SEO Optimization:**
- Built-in support for common SEO patterns;
- Structured data (JSON-LD) helpers;
- Social media meta tags;
- Language and charset management.

---
## 1) Installation:
Install it as a front-end's core-dependency:
```bash
npm install @unhead/vue
```

---
## 2) Define Unhead versions range for future updates:
In `/frontend/package.json` define the limit version for Unhead updates (it should be declared in the project's [TDD](/javascript/document-templates/techical-design-document-tdd.md)):
```json
{
	//...
	"dependencies": {
		//...
		"@unhead/vue": ">=3.4.3 <4.0.0",
	}
}
```

---
## 3) Integration:
Make a decision:
- For SPA architecture: [/javascript/web-development/frontend/vue/component-libraries/unhead/architecture-spa-integrations](javascript/web-development/frontend/vue/component-libraries/unhead/architecture-spa-integrations.md)
- Or for MPA architecture: [/javascript/web-development/frontend/vue/component-libraries/unhead/architecture-mpa-integration](javascript/web-development/frontend/vue/component-libraries/unhead/architecture-mpa-integration.md)

---




