#### JavaScript > Linter, Formatter & Type checker
# Prettier formatter: installation/integration

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

- [x] **1) Install the Prettier extension for the IDE!** (Tip: [related it to a VSCode profile](/ide/vscode/_vscode-knowledge.md))

- [x] **2) Integrating Prettier with the IDE as a formatter:**
Make sure your VSCode user profile (`Ctrl + Shift + P` > `User Preferences`) or project (`/your_project_root/.vscode/settings.json`) is working properly with JS:
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

// TYPESCRIPT SETTINGS
"[typescript]": {
	"editor.defaultFormatter": "esbenp.prettier-vscode", // Prettier
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

- [x] **3) Add the Prettier config file in your `/frontend/` folder:**
In `/your_project_root/frontend/.prettierrc`:
```js
{
	"printWidth": 100,
	"semi": true,
	"singleQuote": false,
	"useTabs": false,
	"tabWidth": 4,
	"bracketSpacing": true,
	"arrowParens": "avoid",
	"trailingComma": "es5"
}
```
        
- [x] **4) (If applicable / Optional) For Python projects, make sure the `pyproject.toml` has a Prettier note there too:**
In `pyproject.toml`:
```toml
...

# Prettier formatter settings:
# Some IDE behaviors for Prettier you find in /.vscode/settings.json
# All core settings of Prettier you find in /frontend/.prettierrc
```

---



