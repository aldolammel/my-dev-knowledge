#### JavaScript > Back-end > Node
# Node.js: installing WITHOUT version control (NOT recommended)

---
                
==To think:==
Installing Node without version control, beyond security issues once the installation will be available for all OS users, it's much more harder to provide maintenance, tests and updates in this approach. Extremely advised to use a version control for Node, and isolate the installation just for your OS account, [using this other roadmap](javascript/web-development/backend/nodejs/1-installation.md).

---
## Check if you already have it without version control:
```bash
which nodejs    # It nothing returns, you are free of a Node without version control.
```

---
## Installing it without version control:
No matter where you are in Terminal, installing Node.js and its NPM (Node Package Manager):

For Ubuntu:
```bash
sudo apt install nodejs npm
```

Check again:
```bash
which nodejs
```

---

