#### JavaScript > Vue > Linter, Formatter & Type checker > Prettier
# Prettier integration for Vue

---

Prettier - installation and integration: [/javascript/linter-formatter-typechecker/prettier/installation](/javascript/linter-formatter-typechecker/prettier/installation.md)

---
## Before:
1. If you wanna a better formatter for Vue, use *ESLint-plugin-for-Vue*: [/javascript/web-development/frontend/vue/linter-formatter-typechecker/eslint-plugin-vue/\_about](javascript/web-development/frontend/vue/linter-formatter-typechecker/eslint-plugin-vue/_installation.md)
2. Case you're using VSCode as IDE, assuming you already installed Prettier in your IDE/project: [/javascript/linter-formatter-typechecker/prettier/installation](/javascript/linter-formatter-typechecker/prettier/installation.md)

---
## 1) Using Prettier as Vue formatter (Not recommended):
In `/.vscode/settings.json`:
```json
// VUE SETTINGS
"[vue]": {
	"editor.defaultFormatter": "esbenp.prettier-vscode",
	"editor.tabSize": 2,
	"editor.indentSize": "tabSize",
	"editor.insertSpaces": true,
},
```

---
