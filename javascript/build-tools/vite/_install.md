#### JavaScript > Build-tool
# Vite

---

https://vite.dev/

Vite (pronounced "veet", and from the same creator of Vue.js) is a JS build-tool and a front-end development server running over Node.js (engine), and it's used in JS and TypeScript projects. It's used primarily to solve the performance and experience problems that come with traditional build-tools like [Webpack](/javascript/build-tools/webpack/_about.md) when projects grow large. And Vite is [framework-agnostic](/dev-concepts/agnostic.md) so through its plugins, Vite can support Vue, React, Svelte, Solid, for example.

---
## 1) Checking if the project have Vite installed:
- [x] **Make a choice:**
	- 1A) This project has NO `/node_modules/` folder yet.
	- 1B) This project already got the `/node_modules/` folder.

......................................

### 1A) This project has NO `/node_modules/` folder yet
- [x] Info: when Vite is correctly installed in a project, Vite belongs to the `/node_modules/` folder. If this folder doesn't exist yet, there's no Vite installed at all.

......................................

### 1B) This project already got the `/node_modules/` folder

- [ ] **Before:** 
	- Assuming you're in the same folder level of the `/node_modules/` one.

- [ ] **1.1) Check it:**
```bash
npm list vite
# Output: if no vite on list, no vite install.
```

- [ ] **1.2) (If applicable) Updating/Reinstalling Vite:** [/javascript/build-tools/vite/updating-reinstalling-vite](javascript/build-tools/vite/updating-reinstalling-vite.md)
	- 1.2.1) After that, skip only the installation steps.

---
## 2) Install Vite:
- [x] Make a decision:
	- 2A) Install Vite for the first time in a new project, and start the scaffolding tool.
	- 2B) Re-install Vite in an existing project: [/javascript/build-tools/vite/updating-reinstalling-vite](/javascript/build-tools/vite/updating-reinstalling-vite.md)

......................................

### 2A) Install Vite for the first time in a new project, and start the scaffolding tool
- [x] 2A.1) On terminal, make sure you are in the project folder root (back-end folder)!
- [x] 2A.2) (If applicable) If you already have a `/frontend/` folder, rename it temporarily (e.g. `/_frontend/`).
- [x] 2A.3) Install Vite and start the project constructor (scaffolding tool):
```bash
npm create vite@latest
# Using 'create', it will install Vite, set it as a dev-dependency on the package.json, and start the project creation scaffolding!
```

**Vite scaffolding:**
- Project name = by convention, use `frontend` (or if you couldn't rename your `frontend` folder, restart the Vite installation and then use "." as the project name).
- Framework = Select what you need for this project like Vue, React, etc...
- Variant = TypeScript or JavaScript
- Install with NPM now = Yes
- (Old questions) In case it's asked:
	- Router? Case this project's adopting [SPA](/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture.md) architecture, yes.
	- CSS Pre-processors? Yes but later!	Vite 6+ has native support for: `.scss`, `.sass`, `.less`, `.styl`, `.stylus`.
	- Babel? No: Vite already convert JS code for all browsers.
	- Linter and formatter? Yes but later! Vite has NO standard solution.

- [x] 2A.4) (If applicable) After the Vite installation and the front-end project folder creation (with a `/node_modules/` in), move files you got in that (renamed) `_frontend` folder to the new one, carefully!

---
## 3) Vite extra integration:
- [x] 3.1) In `/frontend/vite.config.js` (or `.ts`) file:
```js
//...
import path from "path";

export default defineConfig({
	plugins: [...],
	resolve: {
		alias: {
			// "@" in Vite means the path starts from ./src folder, no matter how deep's the caller:
			"@": path.resolve(path.dirname(new URL(import.meta.url).pathname), "./src"),
		},
	},
	// Defining what folder Vite will compile the project when it's ready to production environment:
	publicDir: "public",
});
```
- [x] 3.2) (If applicable) For projects using TypeScript, teach this `@` alias also to TypeScript and Vue itself, editing `/frontend/tsconfig.app.json`:
```js
{
	//...
	"compilerOptions": {
	  "paths": {
	    "@/*": ["./src/*"]
	  },
	  //...
	},
	//...
}
```
---
## 4) (Optional) About some boilerplate files:
Personally, I (@aldolammel) don't like a few Vite front-end config files isolated in the `/frontend/` folder:

- [x] 3.1) Delete the `/frontend/README.md` because you that need this. The project details should be documented in a [TTD](/web-development/document-templates/tdd.md). 

- [x] 3.2) Delete the `/frontend/.gitignore` because that configs already are in the `/.gitignore` file (root).

- [x] 3.3) Delete that folder `/frontend/.vscode/` and its content (no worries about its content, it will be review further in other roadmap)

Done!

---
