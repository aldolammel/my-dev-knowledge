#### JavaScript > Linter, Formatter & Type checker
# Vue-volar

---

Vue-volar is the language tooling type checker that provides syntax highlighting for `.vue` files, IntelliSense, go-to-definition, and TypeScript type-checking inside `<script setup>` and `<template>`. It doesn’t enforce code style or catch bad patterns.

---
## 1) Configure your IDE:

Using VSCode:
- Install the Vue extension!

---
## 2) Integrating on the project:

In `/your_project/.vscode/settings.json`:
```json
"[vue]": {
	"editor.defaultFormatter": "Vue.volar",  // Vue 3 support
	"editor.tabSize": 2,
	"editor.indentSize": "tabSize",
	"editor.insertSpaces": true, 
	"editor.formatOnSave": true,
},
```

In `/your_project/.vscode/extensions.json`:
```json
{
	"recommendations": [
		// ...
		// JS/VUE:
		// "johnsoncodehk.volar", // ?????.
		"Vue.volar",  // Support for Vue 3 (type checking, IntelliSense, autocomplete).
	]
}
```


---


