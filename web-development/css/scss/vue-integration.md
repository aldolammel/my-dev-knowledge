#### Web development > Front-end > CSS > SCSS
# `.scss`/`.sass` integrated with Vue projects

---

Vue SFC (`.vue` files) supports `<style>` blocks with pre-processors like `.sass`/`.scss`. 

After installing this package below, you can write like this in `.vue` files, e.g.:
```html
<style lang="scss" scoped>
.container {
	.title {
		color: blue;
		
		&:hover {
			color: red;
		}
	}
}
</style>
```

---
## 1) Install the SASS/SCSS Compiler:
[/web-development/frontend/css/scss/\_installing-scss-compiler](/web-development/css/scss/_installing-scss-compiler.md)

---
## 2) Integrate it with the project build-tool:
- For Vite: [/web-development/css/scss/build-tool-vite-integration](/web-development/css/scss/build-tool-vite-integration.md)
- For Vue-CLI: /xxxxxxxxxxx
- For Nuxt: /xxxxxxxxxx

---
## 3) (If applicable) In all Vue components (`.vue`) using CSS, include the language in `<style>` tag:
E.g., `.scss`/`.sass`:
```html
<style lang="scss" scoped>
```
No worries about this if you don't reach this part of the front-end's development yet.

---






