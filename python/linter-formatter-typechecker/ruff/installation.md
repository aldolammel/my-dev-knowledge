#### Python > Linter, Formatter & Type checkers
# Ruff

---

Ruff is a high-performance [linter](/dev-concepts/tool-linter.md) and code [formatter](/dev-concepts/tool-formatter.md) for Python, developed by Astral. It's notable for its exceptional speed, largely attributed to being written in Rust. 

**If checks:**
- Python syntax errors.
- Import sorting.
- Code style (PEP 8).
- Bugs.
- Complexity.
- Etc.

TIP: Ruff is developed by the same company of the UV Package manager, so both are completely integrated: [/python/package-manager/uv/\_about-install-and-update](/python/package-manager/uv/_about-install-and-update.md)

---
## 1) Installation:

- [ ] **Before:**
1.  You are in the right `.venv`.

- [ ] **Installing:**
```bash
# Using UV:
uv add --group dev ruff
```

Or using PIP:
```bash
xxxxxxxxxxxxxxxxxxxxxx
```
In this case, don't forget to add this dependency in the project [requirements-dev.txt](python/requirements-dev-txt.md).

---
## 2) Integration:

- [ ] 2.1) (Optional) If using `.gitignore` file, add these lines:
```txt
### Python Linter/Formatter ###
.ruff_cache/
```

- [ ] 2.2) (If applicable) If your project is using `pyproject.toml` instead of `requirements-dev.txt`, include these configures in there: [/python/linter-formatter-typechecker/ruff/pyproject.toml](/python/linter-formatter-typechecker/ruff/pyproject.toml)

- [ ] 2.3) (Optional) Install the Ruff extension for your favorite code IDE!

- [ ] 2.4) (If applicable) In `/project_root/.vscode/settings.json`, add this:
```json
// PYTHON SETTINGS
...
"[python]": {
	"editor.defaultFormatter": "charliermarsh.ruff", // Ruff Linter/Formatter
	"editor.codeActionsOnSave": {
		"source.fixAll.ruff": "always", // Ruff Linter/Formatter
		"source.organizeImports.ruff": "always", // Ruff Linter/Formatter
	}
},

// FILES
"files.exclude": {
	...,
	"**/.ruff_cache": true,
},
"search.exclude": {
	...,
	"**/.ruff_cache": true,
}
```


---

