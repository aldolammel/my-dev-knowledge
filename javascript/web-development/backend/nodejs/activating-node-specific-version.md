#### JavaScript > Back-end > Node
# Activating a specific installed Node version

---
## Before:
- Assuming you already have Node.js installed with version control: [/javascript/web-development/backend/nodejs/1-installation](/javascript/web-development/backend/nodejs/1-installation.md)
- If you wanna active a Node version for a specific project, you must be in any project's folder level!

---
## Activating:
```bash
# Active the version declared in the project's .nvmrc file:
nvm use
# Or a specific other version:
nvm use 26.13.1
```
Make sure it's selected:
```bash
# Only the selected version:
nvm current
# The selected along all available ones:
nvm list node
```

---
## Case you wanna make the project's Node selection automatic:
[/javascript/web-development/backend/nodejs/2.1-automating-switch-process](/javascript/web-development/backend/nodejs/2.1-automating-switch-process.md)



