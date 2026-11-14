#### JavaScript > Vue
# VSCode: basic for Vue project

---

==Important==
Don't do anything from here in cause your project has a [Technical Design Document (TDD)](/python/web-development/django/document-templates/tdd.md) (or similar), describing which formatter, linter and/or type-checker Vue must use.

---
## Basic candidate solution:
- Vue formatter (`.html`, `.css`, `.js`, `.ts`): Prettier
- Vue type checker and linter: Vue-volar (Vue built-in solution)

**If you disagree, here are the options:** 
- Linter for Vue: [/javascript/web-development/frontend/vue/linter-formatter-typechecker/\_linter/vue-options](/javascript/web-development/frontend/vue/linter-formatter-typechecker/_linter/vue-options.md)
- Formatter for Vue: [/javascript/web-development/frontend/vue/linter-formatter-typechecker/\_formatter/vue-options](/javascript/web-development/frontend/vue/linter-formatter-typechecker/_formatter/vue-options.md)
- Type-checker for Vue: [/javascript/web-development/frontend/vue/linter-formatter-typechecker/\_type-checker/vue-options](/javascript/web-development/frontend/vue/linter-formatter-typechecker/_type-checker/vue-options.md)

**Otherwise, stay here and do it!**

---
## 1) Install Prettier as the formatter solution:
[/javascript/linter-formatter-typechecker/prettier/installation](/javascript/linter-formatter-typechecker/prettier/installation.md)

---
## 2) Install extensions:
2.1) IDE extension: Vue extension in your IDE - https://marketplace.visualstudio.com/items?itemName=Vue.volar

---
## 3) VSCode configuration:
In `/.vscode/settings.json`:
```json
// JAVASCRIPT & TYPESCRIPT SETTINGS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"[javascript]": {
	"editor.defaultFormatter": "esbenp.prettier-vscode", // Prettier
	"editor.tabSize": 2,
	"editor.indentSize": "tabSize",
	"editor.insertSpaces": true,
},
"[typescript]": {
	"editor.defaultFormatter": "esbenp.prettier-vscode", // Prettier
	"editor.tabSize": 2,
	"editor.indentSize": "tabSize",
	"editor.insertSpaces": true,
},
```
In `/.vscode/extensions.json` (don't place it inside the `/frontend/` folder):
```json
{
	"recommendations": [
		// JS/VUE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
		"Vue.volar", // Built-in Vue 3 support (basic type checking, IntelliSense, autocomplete).
	]
}
```

