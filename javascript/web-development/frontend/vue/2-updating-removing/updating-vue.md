#### JavaScript > Vue
# Updating Vue in an existing app

---
## Before:
1. It could be important to update the *Node.js* if possible for your project: [javascript/nodejs/0-new-project/update-node-version](javascript/nodejs/0-new-project/update-node-version.md)
2. Assuming you already got Vue installed correctly: [javascript/web-development/frontend/vue/1-install-and-first-steps/0-vue-installation-and-setup](javascript/web-development/frontend/vue/1-install-and-first-steps/0-vue-installation-and-setup.md)

---

## 1) Go to the Vue project folder:

E.g. /app_root_folder/frontend/


---

## 2) Make a choice, which Node package manager are you using:
- 2A) Using NPM;
- 2B) Using Yarn;

### 2A) Using NPM

**2A.1)  Check the Vue version:**
```
npm list vue
```

**2A.2) Once you notice an opportunity to update it:**

Make a choice, which update approach you wanna go:
- Safe;
- Or advanced;

**Safe** > Updating Vue, but ignoring major updates (e.g. from 3.3.x to 3.5.x):
```
npm update vue
```
If some vulnerability is detected:
```
npm audit fix
```

**Advanced** > Updating Vue directly to latest version available, but make sure it won't broken your app! Once you're confident:
```
npm install vue@latest
```
==Remember!==
If you're using [Vite](javascript/build-tools/vite/0-vite.md), no worries, Vite is NOT a package manager.

### 2B) Using Yarn

Soon...


---

## 3) Make sure package.json was updated:

Once you update Vue in your project, */frontend/package.json* file must be updated about Vue version for this project. But *package-lock.json* and *yarn.lock*, for example, are auto-regenerated so don't touch them.


---


## 4) (Optional / If applicable) AI prompts update:

Update the stack information of the app in its AI prompts;

---
