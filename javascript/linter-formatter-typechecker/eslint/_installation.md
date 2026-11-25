#### JavaScript > Linter, Formatter & Type checker
# ESLint: Installation and integration

---
## Before:
- What is ESLint: [/javascript/linter-formatter-typechecker/eslint/\_about](/javascript/linter-formatter-typechecker/eslint/_about.md)

---
## 1) Installation:
Installing with ESLint scaffolding:

- [x] 1.1) Installing and starting the scaffolding:
```bash
# Using NPM:
# 'init' always will install ESLint as dev-dependency, and then start the scaffolding automatically.
npm init @eslint/config@latest
```

- [x] 1.2) Scaffolding selections based on the project:

| Scaffolding questions                              | Vue + TypeScript project selections                                   |
| -------------------------------------------------- | --------------------------------------------------------------------- |
| What do you want to lint?                          | *JavaScript* (no more options in here)                                |
| How would you like to use ESLint?                  | *"To check syntax and find problems"*                                 |
| What type of modules does your project use?        | *"JavaScript modules (import/export)"*                                |
| Which framework does your project use?             | Select what the project demands!                                      |
| Does your project use TypeScript?                  | Select what the project demands!                                      |
| Where does your code run?                          | *"Browser"*                                                           |
| What format do you want your config file to be in? | *"JavaScript"* (more conservative and widely supported for this case) |
Check if everything's right on the front-end folder's `package.json` file!

- [x] 1.3) (If applicable) Issues with vulnerabilities? When *MODERATE* or lower severity, during the development phase, it's not a big deal. Try to update Node components: [/javascript/web-development/backend/nodejs/3.1-updating-component](javascript/web-development/backend/nodejs/3.1-updating-component.md)

- [x] 1.4) (If applicable) Install the ESLint extension (by Microsoft) in your IDE (Tip: [related it to a VSCode profile](/ide/vscode/_vscode-knowledge.md)).

---
## 2) Integration:
- [x] 2.1) In `/frontend/` folder, make sure the ESLint config file structure respect this presets from the file template below:
	- For `eslint.config.js`: [/javascript/linter-formatter-typechecker/eslint/eslint.config-js](javascript/linter-formatter-typechecker/eslint/eslint-config-js.md)
	- For `eslint.config.ts`: not recommended.

- [x] 2.2) (If applicable) For TypeScript projects, add/edit these lines: [/javascript/linter-formatter-typechecker/eslint/eslint-config-for-typescript-support](/javascript/linter-formatter-typechecker/eslint/eslint-config-for-typescript-support.md)

- [x] 2.3) (If applicable) For Vue projects, add/edit these lines: [/javascript/linter-formatter-typechecker/eslint/eslint-config-for-vue-support](/javascript/linter-formatter-typechecker/eslint/eslint-config-for-vue-support.md)

- [x] 2.4) ESLint integration with the IDE:
	- For VSCode: [/javascript/linter-formatter-typechecker/eslint/vscode-eslint](javascript/linter-formatter-typechecker/eslint/vscode-eslint.md)

- [x] 2.5) (If applicable) Make the project build-tool recognizes the ESLint work:
	- For Vite: [/javascript/linter-formatter-typechecker/eslint/vite-plugin-eslint](/javascript/linter-formatter-typechecker/eslint/vite-plugin-eslint.md)

- [x] 2.6) (Optional) Add the ESLint as a script in `package.json` file in the `/frontend/` folder to make ESLint terminal commands available: [/javascript/linter-formatter-typechecker/eslint/package-json](/javascript/linter-formatter-typechecker/eslint/package-json.md)

- [x] 2.7) (If applicable) In case of Git versioning, add it in your `.gitignore` file:
```txt
### Node.js ###
...
# Optional eslint cache
.eslintcache
```

- [x] 2.8) (If applicable / Optional) In case your project has a Python back-end, open the `pyproject.toml` file and include this note in there:
```toml
...

# ESLint linter settings:
# Some IDE behaviors for ESLint you find in /.vscode/settings.json
# All core settings of ESLint you find in /frontend/eslint.config.js
```

Done!

---




