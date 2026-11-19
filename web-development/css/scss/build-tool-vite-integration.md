#### Web development > Front-end > CSS > SCSS
# `.scss`/`.sass` integrated with Vite build-tool

--- 
## 1) Enable the use of global variables through SCSS/SASS files:
In `/frontend/vite.config.js` or `/frontend/vite.config.ts`:
```js
//...

export default defineConfig({
	//...
	plugins: [...],
	//...
	css: {
		preprocessorOptions: {
			scss: {
				additionalData: `@use "@/assets/styles/vars" as *;`,
				quietDeps: true, // Handling deprecation warnings!
			}
		}
	},
	//...
})
```

---
## For `.less` (an alternative Vite built-in solution too):
[web-development/css/less/vue-integration](web-development/css/less/vue-integration.md)

