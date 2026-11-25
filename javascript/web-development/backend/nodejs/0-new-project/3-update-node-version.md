#### JavaScript > Back-end > Node > Project types
# Updating Node.js version

---

==FUNDAMENTAL AND CRITICAL==
Node.js itself always will be installed isolated in your system, never tied to a specific project. What you can (MUST) tied to a specific project folder are Node dependencies that your project requires. In other words, what defines if a Node.js installation is LOCAL or GLOBAL is where and how Node dependencies were installed, and not where Node itself is installed on the OS.

**Updating Node itself:**
- **With** version control: using a version manager command, like `nvm`, it also isolates the installation only for the current OS user.
- **Without** version control: using the OS binary installer, like Ubuntu's `apt`, the installation is available for all OS users.

**Updating Node dependencies:**
- **Local** dependencies updates (using a Node package manager like `npm`): dependencies will be updated in a project's `/node_modules/` folder.
- **Global** dependencies updates (using Node package manager like `npm` with `-g` flag): dependencies will be updated directly in the OS system folders, not tied to a specific project.

---
## Before:
- Check if you don't have Node installed without version control (awful approach): [/javascript/web-development/backend/nodejs/4-uninstall](javascript/web-development/backend/nodejs/4-uninstall.md)

---
## 1) Check what the current project's Node version:
[/javascript/web-development/backend/nodejs/activating-node-specific-version](javascript/web-development/backend/nodejs/activating-node-specific-version.md)

---
## 2) Update the OS:
- For Debian/Ubuntu: [/os/linux/distros/debian/2-updates/update](/os/linux/distros/debian/2-updates/update.md)
- For Fedora: [/os/linux/distros/fedora/2-updates/update](/os/linux/distros/fedora/2-updates/update.md)

---
## 3) Update the Node version constraint in `package.json` file:
```json
// It doesn't make Node be installed in the project's `/node_modules/`, but just warns the user cause they try to change it without change it here first!
{
	"engines": { "node": ">=26.13.1 <27" },
	// ...
}
```

---
## 4) (If applicable) Update the Node version in an existing switch: 
Probably, this project has a kind of Node version switch file (semi-auto or automatic). If so, update it:
- 4A) Project using `.nvmrc` file.
- 4B) Or using `~/.bashrc`.

......................................

### 4A) Using `.nvmrc` file
In your project root folder (back-end folder), open the `.nvmrc` file, and update the Node version (exact version only) manually!
            
......................................

### 4B) Or using `~/.bashrc`
Soon...

---
## 5) Rebuild/Re-sync project's Node dependencies:
[/javascript/web-development/backend/nodejs/syncing-node_modules](javascript/web-development/backend/nodejs/syncing-node_modules.md)

---
## 6) Update the Node version constraint in the project's TDD:
Once everything is running fine, you should find the old Node version constraint in the project's [TDD](/python/web-development/django/document-templates/tdd.md), and then update that.

---
