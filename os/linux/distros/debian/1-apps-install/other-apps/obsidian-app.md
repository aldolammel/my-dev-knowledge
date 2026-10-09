#### Essential @aldolammel's apps
# Obsidian App

---

Obsidian is a powerful, markdown-based knowledge base and note-taking app that works on top of a local folder of plain text files.

---
## 1) Installing:

1.1) Once Obsidian has no an official Debian/Ubuntu APT repository or a trusted PPA (third-party software repository), download the .deb file from: https://obsidian.md/download

1.2) On terminal, go to the folder where the downloaded file is available.

1.3) Close the Obsidian case it still open.

1.4) Run it:
```bash
sudo apt install ./<filename>.deb
```

1.5) Test it and done.

---
## 2) Configuration:

### Obsidian repo settings
For every new vault using a repository, set it through the vault's `.gitignore` file. It will block the commits to upload the `./obsidian/workspace.json` file.
(Info: that `.json` stores, for example, which tabs were opened in a local machine).
```
### Obsidian ###
.obsidian/workspace.json
```
### Extension: Code Files by Lukas Bach
Should Open these file types:
```
ts,tsx,js,json,jsx,py,vue,html,css,scss
```
### Extension: Show All Hidden Files by Anatolii Kmetiuk
Should show files and folders that start with '.' (dot) too:
E.g. `.env`,  `.venv`.
### Extension: Global Search and Replace by Mahmoud Fawzy Khalil
It allows you to search and replace text from everywhere in your vault, and not just in the current file as the native Obsidian feature does today.
### Extension: Omnisearch by Simon Cambier
A better search engine to replace this dummy native search system in Obsidian.
### Extension: LanguageTool Integration by clemens-e
Obvious reasons.
### Obsidian shortcuts
[/\_basic-obidian-shortcuts](/_basic-obidian-shortcuts.md)


---

