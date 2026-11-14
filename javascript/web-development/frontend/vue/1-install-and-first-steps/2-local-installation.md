#### JavaScript > Vue > Project types > Initial roadmap
# Creating a local Vue project

---
## Before:
1. [x] Assuming you already got Node.js: [/javascript/web-development/frontend/vue/1-install-and-first-steps/0-vue-installation-and-setup](/javascript/web-development/frontend/vue/1-install-and-first-steps/0-vue-installation-and-setup.md)
2. [x] Check which back-end folder structure Vue must respect to avoid conflicts:
	- Using Django as back-end: [/javascript/web-development/frontend/vue/1-install-and-first-steps/project-folder-structure-vue-and-django](/javascript/web-development/frontend/vue/1-install-and-first-steps/project-folder-structure-vue-and-django.md)
	- Using Flask as back-end: [/javascript/web-development/frontend/vue/1-install-and-first-steps/project-folder-structure-vue-and-flask](/javascript/web-development/frontend/vue/1-install-and-first-steps/project-folder-structure-vue-and-flask.md)
3. [x] Assuming you already decided which Vue project approach you wanna build up: [/javascript/web-development/frontend/vue/vue-knowledge/SPA-vs-MPA](/javascript/web-development/frontend/vue/vue-knowledge/SPA-vs-MPA.md)

---
## 1) Choosing the build-tool to use:
- [x] **Make a decision:**
	- 1A) Using Vite to install Vue.
		- Vite is the new standard for Vue 3, faster Command Line Interface, created by Vue team.
	- 1B) Or using Vue-CLI to install Vue.
		- Vue-CLI is the old Vue standard Command Line Interface / Webpack-based.

......................................

### 1A) Using Vite to install Vue

- [x] 1A.1) Install Vite and Vue: [/javascript/build-tools/vite/0-vite](/javascript/build-tools/vite/0-vite.md)

- [x] 1A.2) Declare the Node version constraint in the brand new `/frontend/package.json` file (you should find the Node version constraint in project's [TDD](/python/web-development/django/document-templates/tdd.md)):
```json
// It doesn't make Node be installed in the project's `/node_modules/`, but just warns the user cause they try to change it without change it here first!
{
	"engines": { "node": ">=26.13.1 <27" },
	// ...
}
```
      
- [x] 1A.3) Edit the current `/frontend/src/main.js` (or `/frontend/src/main.ts`) with my style version: [/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/project_root/frontend/src/main-initial-version](/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/project_root/frontend/src/main-initial-version.md)

- [x] 1A.4) Run Vue to test it: [/javascript/web-development/frontend/vue/vue-knowledge/\_running-app](/javascript/web-development/frontend/vue/vue-knowledge/_running-app.md)

- [x] 1A.5) Vite fine configs (recommended), in `/frontend/vite.config.js` (or `.ts`) file:
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

- [x] 1A.6) (If applicable / Optional) Extending Vite features (what should be listed in the project's [TDD](/javascript/document-templates/techical-design-document-tdd.md)):
	- CSS Pre-processors (Vite built-in solutions): [/web-development/frontend/css/scss/vue-integration](/web-development/frontend/css/scss/vue-integration.md)

......................................

### 1B) Or using Vue-CLI to install Vue
More about in https://cli.vuejs.org/
		
Install Vue-CLI globally (-g):
```bash
npm install -g @vue/cli
```
Checking installation:
```bash
vue --version  # 'vue' command means 'vue-cli' and not the Vue itself.
```

==IMPORTANT==
Check if the Vue-CLI is attached to the right Node.js version, looking for this line in the terminal right after the Vue-CLI installation is finished:
```bash
"npm warn EBADENGINE   current: { node: 'v24.0.1', npm: '11.3.0' }"
```

**If node version is NOT what you want, do it:**
- A) Switch the Node version to use: [javascript/nodejs/2.1-automating-switch-process](javascript/nodejs/2.1-automating-switch-process.md)
- B) Re-install the Vue-CLI!

Start the project creation:
If you don't got a Vue Project Folder yet:
```bash
vue create <project_name>
```
Otherwise, and if you already are in there:
```bash
vue create .
```
Just follow the prompt instruction options!
		
**Recommended Vue-CLI settings:**
- A) Select "Manually select features"!
- B) Select Vue version 3;
- C) Select the options:
	- Router (Vue-router official solution);
	- Babel (make your JS lines more compatible with modern browsers);
	- CSS Pre-processors (support to scss/sass/less/stylus);
	- Linter / Formatter (code checker);
- D) Select "Sass/SCSS (with dart-sass)";
- E) Select "ESLint with error prevention only";
- F) Select "Lint on save";
- G) Now be aware:
	- For small projects: select `package.json`;
	- For medium or big projects: select `dedicated config files`;
		
Get in the project folder:
```bash
cd <vue_project_folder>
```
Check what is locally installed:
```bash
npm list
```
Update Vue-CLI:
```bash
# Update globally (-g):
$ npm update -g @vue/cli
# Check the current Vue-CLI version:
$ vue --version
# Check whether Vue-CLI is locally of globally installed:
$ npm list
```
Uninstall Vue-cli:
```bash
# Globally:
$ npm uninstall -g @vue/cli
# Or locally:
$ npm uninstall @vue/cli
# Check if uninstalled:
$ vue --version
```

---
## 2) (Optional) Browser extensions for Vue:
- [x] **What to do:**
	- 2A) This front-end project has them defined in its documentation ([TDD](/javascript/document-templates/techical-design-document-tdd.md), for example).
	- 2B) Or a basic solution: [/javascript/web-development/frontend/vue/browser-extensions/options](/javascript/web-development/frontend/vue/browser-extensions/options.md)

---
## 3) (Optional) Formatter, linter and type-checker for Vue:
- [ ] **To install:**
	- 3A) Check if this front-end project has them defined in its documentation (e.g. [TDD](/javascript/document-templates/techical-design-document-tdd.md)):
		- Vue (basic using JavaScript):
			- ~~Type-checker~~
			- Linter
			- Formatter
		- (If applicable) Vue extended to use TypeScript:
			- TypeScript Type-checker
			- TypeScript Linter (only if SFC/SPA approach)
			- TypeScript Formatter
	- 3B) Or a basic solution: [/javascript/web-development/frontend/vue/ide/vscode/basic-for-vue](/javascript/web-development/frontend/vue/ide/vscode/basic-for-vue.md)

---
## 4) Create the front-end's `.env` file:
- [ ] 4.1) Create an exclusive `.env` file to set the front-end environment variables: [/environment-variables/env-for-local/in-frontend/env](/environment-variables/env-for-local/in-frontend/env.md)
- [ ] 4.2) (Optional) Make sure this new `.env` is ignored by [Git](/versioning/git/_basic.md). This line should be there: `frontend/.env`

---
## 5) Bring the front-end structure's `/src/` folder and its files:
- [ ] Unlike previously Vue roadmaps, now is the time to take manually all `/frontend/src/` folders and critical files! Don't start the front-end development now. Just take what you need!
[/javascript/web-development/frontend/vue/vue-knowledge/1-vue-structure](/javascript/web-development/frontend/vue/vue-knowledge/1-vue-structure.md)

---
## 6) Install all front-end's dependencies:
- [ ] Install every front-end's core and dev dependencies of this front-end's project (what should be listed in the project's [TDD](/javascript/document-templates/techical-design-document-tdd.md)).
	- How to install dependencies: [/javascript/nodejs/3-installing-new-components](/javascript/nodejs/3-installing-new-components.md)

---
## 7) Return to the new Vue project roadmap:
[/javascript/web-development/frontend/vue/1-install-and-first-steps/1-install-new-project](/javascript/web-development/frontend/vue/1-install-and-first-steps/1-install-new-project.md)


