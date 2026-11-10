#### JavaScript > Environment > Node
# Node.js installation

---
## Before:
- What is Node: [/javascript/nodejs/\_about](/javascript/nodejs/_about.md)

---
## 1) Installing Node:

- [ ] **1.1) Check if you already got Node installed:**

Locally:
```bash
node -v
```
If you already have it, leave this roadmap through this one: [/javascript/nodejs/2-updating](/javascript/nodejs/2-updating.md)

Globally:
```bash
which nodejs
```
If this returned something, it extremely advised to uninstall it: [/javascript/nodejs/4-uninstall](/javascript/nodejs/4-uninstall.md)

- [ ] **1.2) Installation approach:**
	- A) Globally, WITHOUT the any version manager (NOT recommended);
	- B) By project, using NVM as Node version manager;
	- C) By project, using Docker instead of NVM;

......................................

### A) Globally, WITHOUT the NVM (NOT recommended)
                
==To think:==
If you prefer or is planning to use the NVM (Node Version Manager), you should take the 'B' path, skipping the entire 'A';

Installing globally:
No matter where you are in Terminal, installing Node.js and its NPM (Node Package Manager):
```bash
sudo apt install nodejs npm
```
Make sure Node is installed globally:
```bash
which nodejs    # It nothing returns, something got wrong!
```

......................................

### B) By project, using NVM

==CRUCIAL:==
Node.js with NVM is NOT installed by project but user. You can define which installed Node.js version should run for each project folder (you'll see it further).

**B.1) Installing NVM (it brings Node + NPM):**

RECOMMENDED:
Check if the installation steps below keeps true: https://nodejs.org

- [ ] B.1.1) Download and install NVM:
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash
```

- [ ] B.1.2) In lieu of restarting the shell
```shell
\. "$HOME/.nvm/nvm.sh"
```

- [ ] B.1.3) Download and install Node.js (it brings the NPM):
```bash
nvm install 24
```

- [ ] B.1.4) Verify versions:
```bash
node -v
npm -v
```
If Node version is not what you want, no worries, keep going!

- [ ] B.1.5) Define which version you wanna work: [/javascript/nodejs/2.1-switch-versions](/javascript/nodejs/2.1-switch-versions.md)

......................................

### C) By project, using Docker instead of NVM as node version manager
Soon!

---
## 2) (If applicable / Optional) Make sure you got the `.gitignore` updated:
[/javascript/nodejs/node-gitignore](/javascript/nodejs/node-gitignore.md)

---
## 3) Installing Node packages/components for your project:
[/javascript/nodejs/3-installing-new-components](/javascript/nodejs/3-installing-new-components.md)

---
## Uninstalling:
[/javascript/nodejs/4-uninstall](/javascript/nodejs/4-uninstall.md)

