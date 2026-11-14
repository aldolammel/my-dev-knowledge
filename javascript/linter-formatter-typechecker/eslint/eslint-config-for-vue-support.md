
---

In `eslint.config.js` (or `.ts`):
```js
//...

// Vue configuration:
{
	files: ["**/*.vue"],
	extends: [pluginVue.configs["flat/essential"]],
	languageOptions: {
		parserOptions: {
			parser: tseslint.parser,
		},
	},
},
```