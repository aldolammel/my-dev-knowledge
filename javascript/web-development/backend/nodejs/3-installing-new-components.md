#### JavaScript > Back-end > Node
# Installing new Node components

---

==REMEMBER:==
While `nvm` takes care of Node.js versions, the `npm` takes care of project's dependencies, watching what you do in the project's folder (where the `/node_modules/` is).

---
## Before:
- Case you want to re-sync/rebuild the `/node_modules/` folder based on the project's `package.json`, skip to: [javascript/web-development/backend/nodejs/syncing-node_modules](javascript/web-development/backend/nodejs/syncing-node_modules.md)
- Assuming you already has Node installed (that automatically brings the Node Package Manager, `npm`): [javascript/web-development/backend/nodejs/1-installation](javascript/web-development/backend/nodejs/1-installation.md)

---
## 1) Installing a new component:

- A) Local dependencies installation, using `npm` (STRONGLY RECOMMENDED).
- B) Global dependencies installation, using `npm` with `-g` flag.

......................................

### A) Local dependencies installation (STRONGLY RECOMMENDED)

**Before:**
- Assuming you already used a build-tool (like [Vite](javascript/build-tools/vite/_install.md)) to define where the project's `/node_modules/` folder will be placed.
- Assuming you're in the same folder level where the project's `/node_modules/` folder is.

Check which current project's Node dependencies are installed:
```bash
npm list
```
Then, install what you need:
```bash
npm install <package_name>
```

......................................

### B) Global dependencies installation
No matter where you are on the terminal:
```bash
npm list
```
Install what you want, using `-g` flag:
```bash
npm install -g <package_name>
```

---


