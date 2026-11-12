#### JavaScript > Linter, Formatter & Type checker
# ESLint: Installation and integration

---
## Before:
- What is it: [/javascript/linter-formatter-typechecker/eslint/\_about](/javascript/linter-formatter-typechecker/eslint/_about.md)

---
## 1) Installation 

Before:
- Assuming you are in the `/frontend/` folder.

- [x] 1.1) Installing ESLint core and its configuration package only as DEV dependencies:

Using NPM:
```bash
npm install -D eslint @eslint/js   # -D means it's a DEV dependency!
```
Or using xxx:
```bash
xxxxxxx
```
Check if everything's right on the front-end folder's `package.json` file!

- [x] 1.2) Install `globals` that's an ESLint configuration package to provide global vars for different environments (browser, node, etc) to ESLint:
```bash
npm install -D globals
```

- [x] 1.3) Install the ESLint extension (by Microsoft) in your IDE;

---
## 2) Integration

- [x] 2.1) Check in `front-end` folder root if you have the `eslint.config.js` file. If not, create it: [/javascript/linter-formatter-typechecker/eslint/eslint.config-js](/javascript/linter-formatter-typechecker/eslint/eslint.config-js.md)

- [x] 2.2) Basic IDE integration for ESLint:
- For VSCode: [/javascript/linter-formatter-typechecker/eslint/vscode-eslint-as-formatter](/javascript/linter-formatter-typechecker/eslint/vscode-eslint-as-formatter.md)

- [x] 2.3) (If applicable) Case you are using Vite as your JS Build-tool, make Vite recognize the ESLint work: [/javascript/linter-formatter-typechecker/eslint/vite-plugin-eslint](/javascript/linter-formatter-typechecker/eslint/vite-plugin-eslint.md)

- [x] 2.4) (If applicable) In case the project's demanding Prettier (formatter), make the ESLint doesn't conflict with that: [/javascript/linter-formatter-typechecker/eslint/integrating-prettier-and-eslint](/javascript/linter-formatter-typechecker/eslint/integrating-prettier-and-eslint.md)

- [x] 2.5) (Optional) Add the ESLint as a script in `package.json` file in the `frontend` folder to make ESLint terminal commands available: [/javascript/linter-formatter-typechecker/eslint/package-json](/javascript/linter-formatter-typechecker/eslint/package-json.md)

- [x] 2.6) (If applicable) In case of Git versioning, add it in your `.gitignore` file:
```txt
### Node.js ###
...
# Optional eslint cache
.eslintcache
```

- [x] 2.7) (If applicable / Optional) In case your project has a Python back-end, open the `pyproject.toml` file and include this note in there:
```python
# ESLint linter settings:
# All settings of that is in `/frontend/eslint.config.js`
```

---



