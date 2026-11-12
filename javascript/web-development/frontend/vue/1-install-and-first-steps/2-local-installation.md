#### JavaScript > Project types > Vue
# Creating a local Vue project

---
## (Preview) Just the simplest model:
[/javascript/web-development/frontend/vue/vue-knowledge/using-composition-api/z-examples/hello-world/index.html](/javascript/web-development/frontend/vue/vue-knowledge/using-composition-api/z-examples/hello-world/index.html)

---
## Before:
1. [x] Assuming you already got Node.js: [/javascript/web-development/frontend/vue/1-install-and-first-steps/0-vue-installation-and-setup](/javascript/web-development/frontend/vue/1-install-and-first-steps/0-vue-installation-and-setup.md)
2. [x] Check which back-end paths Vue must keep away to avoid conflicts:
	- Using Django as back-end: [/javascript/web-development/frontend/vue/1-install-and-first-steps/project-folder-structure-vue-and-django](/javascript/web-development/frontend/vue/1-install-and-first-steps/project-folder-structure-vue-and-django.md)
	- Using Flask as back-end: [/javascript/web-development/frontend/vue/1-install-and-first-steps/project-folder-structure-vue-and-flask](/javascript/web-development/frontend/vue/1-install-and-first-steps/project-folder-structure-vue-and-flask.md)
3. [x] Assuming you already decided which Vue project approach you wanna build up: [/javascript/web-development/frontend/vue/vue-knowledge/SPA-vs-MPA](/javascript/web-development/frontend/vue/vue-knowledge/SPA-vs-MPA.md)

---
## 1) Choosing the scaffolding and build-tool for Vue projects:
- 1A) Vite (New standard for Vue 3, faster Command Line Interface, created by Vue team);
- 1B) Or Vue-CLI (Old Vue standard Command Line Interface / Webpack-based);

......................................

### 1A) Using Vite

- [x] 1A.1) Install Vite: [/javascript/build-tools/vite/0-vite](/javascript/build-tools/vite/0-vite.md)

- [x] 1A.2) Edit the current `/src/main.js` (or `/src/main.ts`) with the my style version: [/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/project_root/frontend/src/main-initial-version](/javascript/web-development/frontend/vue/z-example-structure/aldolammel-style/project_root/frontend/src/main-initial-version.md)

- [x] 1A.3) Run Vue to test it: [/javascript/web-development/frontend/vue/vue-knowledge/\_running-app](/javascript/web-development/frontend/vue/vue-knowledge/_running-app.md)

- [ ] 1A.4) Install every front-end's dependencies of this front-end's project (what should be listed in the project's [TDD](/javascript/document-templates/techical-design-document-tdd.md)).
	- How to install dependencies: [/javascript/nodejs/3-installing-new-components](/javascript/nodejs/3-installing-new-components.md)

- [ ] 1A.5) (Optional) Configure Vite to recognize "@" in paths and more (Recommended):

The at ("@") in Vite projects mean the path starts from `./src` folder, no matter how deep is the caller file is in Vue project folder structure. And `publicDir` you're defining what folder the Vite will compile the project when it's ready to production environment.

In `/frontend/` folder, open the `vite.config.js` file and add these lines:	
```js
import path from "path";

export default defineConfig({
	plugins: [
		//...
	],
	resolve: {
		alias: {
			"@": path.resolve(path.dirname(new URL(import.meta.url).pathname), "./src"),
		},
	},
	publicDir: "public",
	//...
});
```

- [ ] 1A.6) (If applicable / Optional) In case the SCSS/SASS on the project, make Vite to recognize SCSS global vars importable: [/web-development/frontend/css/scss/variables-global](/web-development/frontend/css/scss/variables-global.md)
	 - More SCSS integration we will see later!

- [ ] 1A.7) (If applicable / Optional) Extending Vite features (what should be listed in the project's [TDD](/javascript/document-templates/techical-design-document-tdd.md)):
	- Router (Vue official solution): [/javascript/web-development/frontend/vue/3-component-libraries/vue-router/\_vue-router](/javascript/web-development/frontend/vue/3-component-libraries/vue-router/_vue-router.md)
	- CSS Pre-processors (Vite built-in solutions): [/web-development/frontend/css/scss/vue-integration](/web-development/frontend/css/scss/vue-integration.md)

......................................

### 1B) Or using Vue-CLI
		
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
Check if the Vue CLI is attached to the right Node.js version, looking for this line in the terminal right after the Vue-cli installation is finished:

```
"npm warn EBADENGINE   current: { node: 'v24.0.1', npm: '11.3.0' }"
```

If node version is NOT what you want, do it:

- A) Switch the Node version to use: [/javascript/nodejs/2.2-automating-switch-process](/javascript/nodejs/2.2-automating-switch-process.md)
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
		
Recommended Vue-CLI settings:
A) Select "Manually select features"!
B) Select Vue version 3;
C) Select the options:
- Router (Vue-router official solution);
- Babel (make your JS lines more compatible with modern browsers);
- CSS Pre-processors (support to scss/sass/less/stylus);
- Linter / Formatter (code checker);
D) Select "Sass/SCSS (with dart-sass)";
E) Select "ESLint with error prevention only";
F) Select "Lint on save";
G) Now be aware:
>> For small projects:
select "package.json";
>> For medium or big projects:
select "dedicated config files";
		
Get in the project folder:
```bash
cd <vue_project_folder>
```
Check what is locally installed:
```bash
npm list
```

Update Vue-CLI:
	
		# Update globally (-g):
			$ npm update -g @vue/cli

		# Check the current Vue-CLI version:
			$ vue --version

		# Check whether Vue-CLI is locally of globally installed:
			$ npm list


Uninstall Vue-cli:

			# Globally:
				$ npm uninstall -g @vue/cli
			# Or locally:
				$ npm uninstall @vue/cli
			# Check if uninstalled:
				$ vue --version
	

---
## 2) Create the front-end's `.env` file:
- [ ] 2.1) Create an exclusive `.env` file to set the front-end environment variables: [/environment-variables/env-for-local/in-frontend/env](/environment-variables/env-for-local/in-frontend/env.md)
- [ ] 2.2) (Optional) Make sure this new `.env` is ignored by Git. This line should be there: `frontend/.env`

---
## 3) Make sure you already got configured your code quality shields for Vue:
- Linter for Vue: [/javascript/web-development/frontend/vue/linter-formatter-typechecker/\_linter/vue-options](/javascript/web-development/frontend/vue/linter-formatter-typechecker/_linter/vue-options.md)
- Formatter for Vue: [/javascript/web-development/frontend/vue/linter-formatter-typechecker/\_formatter/vue-options](/javascript/web-development/frontend/vue/linter-formatter-typechecker/_formatter/vue-options.md)
- Type-checker for Vue: [/javascript/web-development/frontend/vue/linter-formatter-typechecker/\_type-checker/vue-options](/javascript/web-development/frontend/vue/linter-formatter-typechecker/_type-checker/vue-options.md)

---
## Back to the installation instructions:
[/javascript/web-development/frontend/vue/1-install-and-first-steps/1-install-new-project](/javascript/web-development/frontend/vue/1-install-and-first-steps/1-install-new-project.md)


