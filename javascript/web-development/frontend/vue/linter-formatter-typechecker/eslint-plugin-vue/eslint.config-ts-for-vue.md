In `/frontend/eslint.config.ts`:
```ts
//...
import pluginVue from "eslint-plugin-vue";


export default defineConfig([
	// ...
	
	// Core configuration:
	{
		files: ["**/*.{js,mjs,cjs,ts,mts,cts,vue}"],
		//...
	},
	
	//...
	
	// Vue recommended rules:
	{
		files: ["**/*.{js,mjs,cjs,ts,mts,cts,vue}"],
		extends: [pluginVue.configs["flat/essential"]],
	},
	
	// TypeScript parser for Vue:
	{
		files: ["**/*.vue"],
		languageOptions: {
			parserOptions: {
				parser: tseslint.parser,
			},
		},
	},
]);
```

---
## JavaScript version:
[/javascript/web-development/frontend/vue/linter-formatter-typechecker/eslint-plugin-vue/eslint.config-js-for-vue](/javascript/web-development/frontend/vue/linter-formatter-typechecker/eslint-plugin-vue/eslint.config-js-for-vue.md)




