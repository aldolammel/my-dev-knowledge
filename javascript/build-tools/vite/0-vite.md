#### JavaScript > Build-tool
# Vite

---

Vite (pronounced "veet", and from the same creator of Vue.JS) is a JS build tool and a front-end development server running over Node.JS (engine), and it's used in JS and TypeScript projects.

https://vite.dev/

It's used primarily to solve the performance and experience problems that come with traditional build tools like Webpack when projects grow large.

And Vite is framework-agnostic so through its plugins, Vite can support Vue, React, Svelte, Solid, for example.

---
## 1) Figure out if Vite is installed and/or update Vite:

**Before:**
- On terminal, if you already have the `/frontend/` (or similar), go in there. If you don't have one, no worries, Vite will create one.

1.1) (If applicable) In cause you have Vite installed, check it:
```bash
npm list vite
```

1.2) (If applicable) Updating Vite: [/javascript/build-tools/vite/updating](/javascript/build-tools/vite/updating.md)

---
## 2) Install Vite:
Which method do you wanna use:
- 2A) Install Vite for the first time in a new front-end project (scaffolding tool);
- 2B) Re-install Vite in an existing front-end project;

......................................

### 2A) Install Vite for the first time in a new front-end project
- [ ] 2A.1) On terminal, go to project's back-end folder (NOT the `/frontend/` folder)!
- [ ] 2A.2) (If applicable) If you already have a `/frontend/` folder, rename it temporarily (e.g. `/_frontend/`).
- [ ] 2A.3) Install Vite locally (without -g) and start the project creation:

```bash
npm create vite@latest
```

This process will create the Vue project folder, asking you the folder's name soon! Follow the prompt:

- Project name = by convention, use `frontend` (or if you couldn't rename your `frontend` folder, restart the Vite installation and then use "." as the project name).
- Framework = Vue
- Variant = TypeScript or JavaScript
- Install with NPM now = Yes
- In case it's asked:
	- Router? In case of SPA project, yes, but later!  (and MPA projects ??????????????). Vite has NO standard solution, but Vue does (Vue-Router)!
	- CSS Pre-processors? Yes but later!	Vite 6+ has native support for: .scss, .sass, .less, .styl, .stylus!
	- Babel? No: Vite already convert JS code for all browsers;
	- Linter/Formatter? Yes but later! Vite has NO standard solution;

- [ ] 2A.4) (If applicable) After the installation, move the files you got in that renamed/old `frontend` folder to the new one, carefully!

......................................

### 2B) Re-install Vite in an existing front-end project

TIP:
Do you need uninstall Vite first? [/javascript/build-tools/vite/uninstall](/javascript/build-tools/vite/uninstall.md)

2B.1) Go to the front-end project folder, e.g.,  `/my_project/frontend/`

2B.2) Re-install Vite:

Using NPM:
	- Install a specific major version (recommended for stability)
```bash
npm install vite@^7    # means the latest version of v7.
```
If you run `vite@latest`, probably you'll face compatible errors with [Tailwind](/web-development/frontend/css/css-libraries-frameworks/tailwind/_about.md) or other frameworks that depends of Vite plugins and are not ready for Vite latest version.

Install the absolute latest version (may cause compatibility issues)
```bash
npm install vite@latest
```
		
Using YARN:
```bash
yarn add vite@^7
```

---
## 3) About some boilerplate files:
3.1) Personally, I (@aldolammel) don't like to use `.gitignore` inside the `/frontend/` folder, so my back-end `.gitignore` file already has those critical front-end ignore stuff.

---
## 4) Plugins for your linter:
Case you're using (or will):
- ESLint: [/javascript/linter-formatter-typechecker/eslint/vite-plugin-eslint](/javascript/linter-formatter-typechecker/eslint/vite-plugin-eslint.md)

---
