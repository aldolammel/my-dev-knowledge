#### JavaScript > Linter, Formatter & Type checker > ESLint
# Integrating ESLint and Prettier

---
## Before:
- Assuming your `frontend` folder already has the Prettier config file: `.prettierrc` [/javascript/linter-formatter-typechecker/prettier/installation](/javascript/linter-formatter-typechecker/prettier/installation.md)
- Assuming you are, on the terminal, in the `frontend` folder.
          
---
## 1) Installing Prettier and critical integration packages:
```bash
npm install -D eslint-config-prettier eslint-plugin-prettier
```
Check if everything's right on the front-end folder's `package.json` file!

---
## 2) Integrating compatibility:
                    
==KEEP IN MIND:==
Once you are here it's because you wanna use Prettier. That said, set all ESlint FORMATTING stuff to Prettier, meanwhile ESLint focuses only in linting!

Adapt this file below in your frontend project to consider Prettier with ESLinter partner: [/javascript/linter-formatter-typechecker/eslint/eslint.config-js-for-prettier](/javascript/linter-formatter-typechecker/eslint/eslint.config-js-for-prettier.md)

Replace the current IDE configuration:
- For VSCode: [/javascript/linter-formatter-typechecker/eslint/vscode-prettier-as-eslint-formatter](/javascript/linter-formatter-typechecker/eslint/vscode-prettier-as-eslint-formatter.md)

---



