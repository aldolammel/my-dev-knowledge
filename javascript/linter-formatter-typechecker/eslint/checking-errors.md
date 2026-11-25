#### JavaScript > Linter, Formatter & Type checker > ESLint
# Checking linting errors

---
## Before:
- What is ESLint: [/javascript/linter-formatter-typechecker/eslint/\_about](/javascript/linter-formatter-typechecker/eslint/_about.md)
- Assuming you already added these script lines in the project's `package.json` file: [/javascript/linter-formatter-typechecker/eslint/package-json](/javascript/linter-formatter-typechecker/eslint/package-json.md)
- If your front-end is Vue, it's assuming you already installed the Vue plugin for ESLint: [/javascript/web-development/frontend/vue/linter-formatter-typechecker/eslint-plugin-vue/\_installation](/javascript/web-development/frontend/vue/linter-formatter-typechecker/eslint-plugin-vue/_installation.md)
- Assuming you are in the `/frontend/` folder.
- (If applicable) For Node installation with version control, active the specific Node for this project: [/javascript/web-development/backend/nodejs/activating-node-specific-version](/javascript/web-development/backend/nodejs/activating-node-specific-version.md)
- (If applicable) Assuming you're in the right Git branch: [command-branch](/versioning/git/command-branch.md) and [command-checkout](/versioning/git/command-checkout.md) 

---

```bash
# Just list issues:
# Using NPM:
npm run lint:check

# List and fix them:
# Using NPM:
npm run lint
```

