#### JavaScript > Build-tool > Vite
# Updating/Reinstalling Vite

---
## Before:
- On terminal, go to the folder where you found the `/node_modules/` folder.
- Assuming you are using the built-in Node Package Manager (`npm`).

---
## 1) Check the current Vite version:
```bash
npm list vite
```

---
## 2) Update the OS:
- For Debian/Ubuntu: [/os/linux/distros/debian/2-updates/update](/os/linux/distros/debian/2-updates/update.md)
- For Fedora: [/os/linux/distros/fedora/2-updates/update](/os/linux/distros/fedora/2-updates/update.md)

---
## 3) Update to the latest Vite version:
No sure if [uninstall Vite](javascript/build-tools/vite/uninstall.md) would make it more solid.

That said, update it to the latest version available:
```bash
npm update vite
```
Or to a specific version (always as dev-dependency in a project):
```bash
npm install -D vite@6.3.5
```
Or to the latest Vite version (may cause compatibility issues):
```bash
npm install -D vite@latest
```
---
## 4) Check again the current Vite version:
```bash
npm list vite
```

---

