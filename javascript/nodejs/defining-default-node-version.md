#### JavaScript > Environment > Node
# Defining a default Node version for an OS user

---
## Before:
- This only works if you've installed Node using a version control!
- This default definition is not by project but OS user (your current account).
- You DON'T need to be in a project folder at all.

---
## 1) List all Node versions installed:
```bash
nvm list node
```

---
## 2)  Active the version you wanna make the default one:
[/javascript/nodejs/activating-node-specific-version](/javascript/nodejs/activating-node-specific-version)

---
## 3) Define the default version based on the active one:
Using NVM:
```bash
nvm alias default node
```

---
