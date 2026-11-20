#### JavaScript > Vue > Linter, Formatter & Type checker
# `vue-tsc` type-checker for Vue using TypeScript
---

A command-line type checking tool for Vue, based on a `tsc` wrapper, enabling the TypeScript compiler to understand `.vue` files.

---
## 1) Installation:

==Vite users:==
The `vue-tsc` is already installed when you have built the Vue project using [Vite](javascript/build-tools/vite/_install.md) scaffolding and selected the TypeScript as its language. If your case, skip the installation step, going to the integration directly! You can make it sure checking the dev dependencies in `/frontend/package.json` file.

For non-Vite project, on the `/frontend/` folder, do it:
```bash
npm install -D typescript vue-tsc
```

---
## 2) Integration:

2.1) In `/frontend/package.json`:
```json
{
	//...
	"scripts": {
		//...  
		"type-check": "vue-tsc --noEmit",
		"build:types": "vue-tsc --declaration --emitDeclarationOnly"
	}
	//...
}
```

2.2) (If applicable / Optional) For Python projects, make sure the `pyproject.toml` has a vue-tsc note there too:  
In `pyproject.toml`:
```toml
...

# vue-tsc TypeScript type-checker settings:
# Some IDE behaviors for TypeScript you find in /.vscode/settings.json
```

---
## Checking type-checker errors:
[javascript/web-development/frontend/vue/linter-formatter-typechecker/vue-tsc/checking-errors](javascript/web-development/frontend/vue/linter-formatter-typechecker/vue-tsc/checking-errors.md)

---



