#### JavaScript > Front-end > Vue
# `.gitignore` file for Vue

---
## Before:
- If you are using `.gitignore`, you should be using [Git](/versioning/git/_basic.md) as your versioning system.

---

(If applicable) Add these lines in your `.gitignore` file:
```
### Node.js ###
node_modules/
jspm_packages/
dist/                         <-- Aware: probably duplicated!
dist-ssr/
*.local

logs
*.log                         <-- Aware: probably duplicated!
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*
.pnpm-debug.log*
# Yarn Integrity file
.yarn-integrity
# yarn v2
.yarn/cache
.yarn/unplugged
.yarn/build-state.yml
.yarn/install-state.gz
.pnp.*

# Editor directories and files
.idea                         <-- Aware: probably duplicated!
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

### Vue.js ###
.vuepress/dist
```

==IMPORTANT:==
Check if the `.gitignore` is NOT duplicated along the project child folder. For example, Vue installation by Vite creates a git file in vue root folder!

---
## About `.gitignore` file:
[/versioning/git/gitignore-file](/versioning/git/gitignore-file.md)



