#### JavaScript > Back-end > Node
# Uninstalling Node.js

---
## Make a decision:
You wanna uninstall:
- A) A project's NPM component.
- B) A global NPM component.
- C) A Node installed with a version control.
- D) A Node installed without version control.
- E) The CDN Node.

......................................

### A) Uninstalling a project's NPM component

Before:
- Assuming you are in the same folder where you see the `/node_modules/` folder in the same level. 

A1) List all component installed locally:
```bash
npm list
```        
A2) Uninstall the desired package/component:
```bash
npm uninstall <package_name>
# e.g.
npm uninstall naive-ui         # without '@' and version numbers

```

......................................

### B) Uninstalling a global NPM component

Before:
- Go to your OS user folder (`/home/` in Ubuntu, for example)

B1) List all component installed globally:
```bash
npm list
```

B2) No matter where you are, uninstall the desired package/component globally (-g):
```bash
npm uninstall -g <package_name>
# e.g.
npm uninstall -g naive-ui     # without '@' and version numbers
```

......................................

### C) Uninstalling a Node installed with a version control

==TIP:==
Maybe you don't need to uninstall. With NVM (Node Version Manager) installed, you can switch the installed version easily: [/javascript/web-development/backend/nodejs/activating-node-specific-version](javascript/web-development/backend/nodejs/activating-node-specific-version.md)

**Before:**
- Assuming you are using NVM/NPM to manage Node packages and stuff.
- Did you make a project's `package.json` backup to help you rebuild `/node_modules/` folder later? Or would you rather use a project [TDD](/python/web-development/django/document-templates/tdd.md) to guide you in installation from the scratch?

C1) Check which versions of Node you got installed in your current OS user:
```bash
# Do it anywhere on the terminal:
nvm list node
```
C2) Uninstall a specific Node version:
```bash
nvm uninstall <version>     # E.g., you can define 23 or an exact version: 23.11.0
```

......................................

### D) Uninstalling a Node installed without version control

D1) Check the Node (`nodejs`)version (not `node` for this case):
```bash
nodejs -v
which nodejs   # if something returned, it's installed globally!
```
D2) (If applicable) Uninstall Node and its package manager:
```bash
sudo apt remove nodejs npm
```
D3) (Optional) Removing configuration files:
```bash
sudo apt purge nodejs npm
```
D4) Removing the uninstalled files:
```bash
sudo apt autoremove
```
D5) Make sure the global Node doesn't exist anymore:
```bash
nodejs -v
which nodejs  # if nothing returned, there's NO global Node anymore!
```
D6) (If applicable) If Node persists globally:
```bash
# Remove global npm packages directory (if it exists)
sudo rm -rf /usr/local/lib/node_modules
# Remove npm cache
sudo rm -rf ~/.npm
# Remove any remaining Node.js related files
sudo rm -rf /etc/apt/sources.list.d/nodesource.list*
```
- D6.1) Close the current Terminal, and check everything once again!

......................................

### E) Uninstalling CDN Node
Soon! Basically just remove that `<head>`'s `<link>` tag!
                    
---



