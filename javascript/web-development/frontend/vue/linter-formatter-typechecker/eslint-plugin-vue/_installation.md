#### JavaScript > Vue > Linter, Formatter & Type checker
# Extending ESLint to Vue projects

---  
    
==BE AWARE FOR SFCs!==
ESLint only add value for a Vue project that uses Single-Files-Components (SFCs), it means, it's using `.vue` files)! Otherwise, this lint won't do nothing.

---
## Before:
- What is ESLint: [/javascript/linter-formatter-typechecker/eslint/\_about](/javascript/linter-formatter-typechecker/eslint/_about.md)

---

This plugin allows ESLint to check the `<template>` and `<script>` of `.vue` files with ESLint, as well as Vue code in `.js` files.

**Checks:** finds errors and enforces style rules.

**Template linting:**
- Vue directive syntax validation (`v-if`, `v-for`, etc.);
- Template expression checking;
- Component prop validation;
- Event handler verification;

**SFC structure validation:**
- Script setup syntax (if you use it);
- Component lifecycle and structure;
- Vue 3 specific patterns and best practices;

---
## 1) Installing:

**Before:**
- Assuming you already have a Vue project installed.
- Assuming you already are in the `/frontend/` folder of the project on terminal.
- Assuming you already installed the ESLint: [/javascript/linter-formatter-typechecker/eslint/\_installation](/javascript/linter-formatter-typechecker/eslint/_installation.md)
- Your Vue application architecture is SPA: [/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture](/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture.md)

**1.1) Install the ESLint plugin for Vue (eslint-plugin-vue) as development dependency:**

https://eslint.vuejs.org/

Using NPM:
```bash
npm install -D eslint-plugin-vue      # -D means DEV dependency!
```
Check if everything's right on the front-end folder's `package.json` file!

**2) Edit the ESLint config file:**
- For `eslint.config.js`: [/javascript/web-development/frontend/vue/linter-formatter-typechecker/eslint-plugin-vue/eslint.config-js-for-vue](/javascript/web-development/frontend/vue/linter-formatter-typechecker/eslint-plugin-vue/eslint.config-js-for-vue.md)
- For `eslint.config.ts`: [/javascript/web-development/frontend/vue/linter-formatter-typechecker/eslint-plugin-vue/eslint.config-ts-for-vue](/javascript/web-development/frontend/vue/linter-formatter-typechecker/eslint-plugin-vue/eslint.config-ts-for-vue.md)

In `/frontend/eslint.config.js`:
REVIEW THISSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```js
// This basic file model: /javascript/Linter-Formatter-Typechecker/eslint/eslint.config.js

import js from "@eslint/js";
import pluginVue from "eslint-plugin-vue"; // <---- ADD IT!
//...

export default [
	js.configs.recommended,
	...pluginVue.configs["flat/recommended"], // <---- ADD IT!
	{
		files: ["**/*.vue", "**/*.js", "**/*.mjs"], // <---- ADD IT!
		languageOptions: {
			parser: pluginVue.parser, // <---- ADD IT!
			ecmaVersion: "latest",
			//...
		},
		rules: {
			"vue/multi-word-component-names": "off", // <---- ADD IT!
			//...
		},
	},
	//...
];
```

**3) (If applicable) In `vite.config.js` file:**
```js
//...
import eslintPlugin from 'vite-plugin-eslint'
//...
	plugins: [
		vue(),
		//...
		eslintPlugin({
			include: ['src/**/*.js', 'src/**/*.vue', 'src/*.js', 'src/*.vue'],
			exclude: ['node_modules/**', 'dist/**'],
			cache: false
		})
	],
```

**4) Basic IDE configs for Vue:**

For VSCode:
- In `/project/.vscode/settings.json` file:
```json
// VUE SETTINGS
"[vue]": {
	"editor.defaultFormatter": "dbaeumer.vscode-eslint", // ESLint
	...
},
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


    

        