#### JavaScript > Environment > Node
# Node.js updating

---

==REMEMBER:==
When you install the NVM, it brings the Node.js and, by consequence, the NPM (the embedded Node Package Manager).

---
## Before:
- Assuming you already got Node installed: [/javascript/nodejs/1-installation](/javascript/nodejs/1-installation.md)
- If you wanna update Node, NPM, and NVM, keep going in this roadmap. Otherwise, skip this and visit this one: [/javascript/nodejs/3.1-updating-component](/javascript/nodejs/3.1-updating-component.md)

---
## 1) Update your OS:
- For Debian/Ubuntu: [/os/linux/distros/debian/2-updates/update](/os/linux/distros/debian/2-updates/update.md)
- For Fedora: [/os/linux/distros/fedora/2-updates/update](/os/linux/distros/fedora/2-updates/update.md)

---
## 2) Checking current versions for the current user:

==IMPORTANT==
Node.js with NVM is NOT installed by project, but user. The user/you can define which installed Node.JS version should run for every project folder.
```bash
nvm -v             # Node Version Manager
nvm list node      # If already available, best way to check Node version!
npm -v             # NPM (Node Package Manager), embedded with NVM.
```

---
## 3) Update (switching to or including the latest version):
[/javascript/nodejs/2.1-switch-versions](/javascript/nodejs/2.1-switch-versions.md)



