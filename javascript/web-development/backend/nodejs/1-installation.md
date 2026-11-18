#### JavaScript > Back-end > Node
# Installing Node.js locally

---

==FUNDAMENTAL AND CRITICAL==
Node.js itself always will be installed isolated in your system, never tied to a specific project. What you can (MUST) tied to a specific project folder are Node dependencies that your project requires. In other words, what defines if a Node.js installation is LOCAL or GLOBAL is where and how Node dependencies were installed, and not where Node itself is installed on the OS.

**Installing Node itself:**
- **With** version control: using a version manager command, like `nvm`, it also isolates the installation only for the current OS user.
- **Without** version control: using the OS binary installer, like Ubuntu's `apt`, the installation is available for all OS users.

**Installing Node dependencies:**
- **Local** dependencies installation (using a Node package manager like `npm`): dependencies will be installed in a project's `/node_modules/` folder.
- **Global** dependencies installation (using Node package manager like `npm` with `-g` flag): dependencies will be installed directly in the OS system folders, not tied to a specific project.

---
## Before:
- [x] What is Node.js: [/javascript/nodejs/\_about](javascript/web-development/backend/nodejs/_about.md)
- [x] Assuming you know the specific version your Node.js project demands (it should be crystal clear in the project's [TDD](/python/web-development/django/document-templates/tdd.md)).
- [x] You DON'T need to be in a project folder at all.

---
## 1) Check if you already have it:

- [x] **1.1) Looking for installed Node without version control:**
```bash
which nodejs
```
If this returned something, it extremely recommended to uninstall it: [javascript/web-development/backend/nodejs/4-uninstall](javascript/web-development/backend/nodejs/4-uninstall.md)

- [x] **1.2) Looking for installed Node with version control:**
1.2.1) Check any Node with version control:
```bash
node -v
```
1.2.2) Check if you have installed the Node Version Manager:
```bash
nvm list node
```
1.2.3) Possible outputs:
- If nothing happened, stay in this current roadmap!
- If  the desired Node version is not listed between others, stay in this current roadmap!
- If you already have it, the target version is on the list, but not selected, active it: [/javascript/web-development/backend/nodejs/activating-node-specific-version](/javascript/web-development/backend/nodejs/activating-node-specific-version.md)
- If you already have it, and it already attempt your project, skip the Node installation itself, but check the next steps in this roadmap!

---
## 2) Installing Node:
- [x] **Make a decision:**
	- A) Install Node with version control.
	- B) Install Node with Docker.
	- C) Install Node WITHOUT version control (NOT recommended): [/javascript/web-development/backend/nodejs/install-node-without-version-control](/javascript/web-development/backend/nodejs/install-node-without-version-control.md)

......................................

### A) Installing Node with version control

- [x] A1) (If applicable) Download and install NVM (Node Version Manager):
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.41.0/install.sh | bash  # link last updated 2026-11 (https://nodejs.org)
```

- [x] A2) Active NVM immediately without restarting your terminal:
```shell
\. "$HOME/.nvm/nvm.sh"
```

- [x] A3) Download and install Node.js (it brings the NPM - Node Package Manager):
```bash
# Latest LTS version:
nvm install --lts
# Or a specific one:
nvm install 26.13.1
```

- [x] A4) (If applicable) In case more than one Node version installed, active the right one: [javascript/web-development/backend/nodejs/activating-node-specific-version](javascript/web-development/backend/nodejs/activating-node-specific-version.md)

- [x] A5) (If applicable / Optional) Defining Node version as the default one for your OS user: [javascript/web-development/backend/nodejs/defining-default-node-version](javascript/web-development/backend/nodejs/defining-default-node-version.md)

- [x] A6) (If applicable / Optional) Automating the switch process by project: [javascript/web-development/backend/nodejs/2.1-automating-switch-process](javascript/web-development/backend/nodejs/2.1-automating-switch-process.md)

......................................

### B) Installing Node with Docker
Soon!

---
## 2) (If applicable / Optional) Make sure you got the `.gitignore` updated:
- [x] [javascript/web-development/backend/nodejs/node-gitignore](javascript/web-development/backend/nodejs/node-gitignore.md)

Done

---
## Uninstalling:
[javascript/web-development/backend/nodejs/4-uninstall](javascript/web-development/backend/nodejs/4-uninstall.md)
## Installing Node components for a project (Local dependencies):
[javascript/web-development/backend/nodejs/3-installing-new-components](javascript/web-development/backend/nodejs/3-installing-new-components.md)

