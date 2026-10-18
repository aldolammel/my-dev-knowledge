PRETTIER FORMATTER: INTEGRATION

---

Prettier is an opinionated code formatter with support for:

- JavaScript (including experimental features)
- JSX
- Angular
- Vue
- Flow
- TypeScript
- CSS, Less, and SCSS
- HTML
- Ember/Handlebars
- JSON
- GraphQL
- Markdown, including GFM and MDX v1
- YAML

---
## Installing/Integrating:

Using VSCode:

**1) Install the Prettier extension for the IDE!**

**2) Integrating Prettier with the IDE:**
Make sure your VSCode user profile (`Ctrl + Shift + P` > `User Preferences`) or project (`/root_app/.vscode/settings.json`) is working properly with JS:

==Important==
If you're integrating [ESLint](/javascript/linter-formatter-typechecker/eslint/_installation.md) to the *Prettier*, and the *ESLint* is already as the JS default formatter, just skip the JS settings here, leaving it to ESLint!

```json
// PROJECT SETTINGS
"prettier.printWidth": 100, // Prettier

// JAVASCRIPT SETTINGS
"[javascript]": {
	"editor.defaultFormatter": "esbenp.prettier-vscode",  // Prettier
	"editor.tabSize": 2,
	"editor.indentSize": "tabSize",
	"editor.insertSpaces": true,
	//"editor.formatOnSave": true,
},

// JSON SETTINGS
"[json]": {
	"editor.defaultFormatter": "esbenp.prettier-vscode", // Prettier
},

// CSS SETTINGS
"[css]": {
	"editor.defaultFormatter": "esbenp.prettier-vscode", // Prettier
},
```

        3) (Optional)

Add the Prettier config file in your frontend folder: `.prettierrc`
In `/your_project_root/frontend/.prettierrc`:
```js
{
  "printWidth": 100,
  "semi": true,
  "singleQuote": false,
  "trailingComma": "es5"
}
```
        
        4) (If applicable) 

For Python projects, make sure the `pyproject.toml` has Prettier basic settings:                
In `pyproject.toml`:
```toml
# Prettier formatter settings:
[tool.prettier]
printWidth = 100
semi = true
singleQuote = false
trailingComma = "es5"
tabWidth = 2
useTabs = false
bracketSpacing = true
arrowParens = "avoid"
```