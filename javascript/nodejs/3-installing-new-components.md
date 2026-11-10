#### JavaScript > Environment > Node
# Installing new Node components

---

==REMEMBER:==
Unlike NVM, the NPM is watching the folder you are running the terminal!

---
## Before:
- Assuming you got NPM (Node Package Manager) installed. Otherwise: [/javascript/nodejs/1-installation](/javascript/nodejs/1-installation.md)
- Go to the project folder (often, in frontend folder). ??????????????????????????????????????????????????????????????????????????????????????????????????????

---
## 1) Installing a new component:

A) Globally;
B) Locally (STRONGLY RECOMMENDED);

......................................

### A) Globally (NOT recommended)
In the project folder, check the current packages are installed on this project:
```bash
npm list
```
No matter where you are, install the desired package/component globally (-g):
```bash
npm install -g <package_name>
```

......................................

### B) Locally (RECOMMENDED)
In your user root folder, check the current packages are installed on this machine:
```bash
npm list
```
So, again, in the project folder, install the desired package/component:
```bash
npm install <package_name>
```

---





