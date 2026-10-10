#### Python > Linter, Formatter & Type checker
# DjLint

---

As an additional tool for any Python linter/formatter and any Django code linter/formatter, DjLint is a Django template linter and a django template formatter.

**It checks:**
- Template syntax errors.
- Formatting.
- HTML structure.
- Template-specific best practices.

---
## 1) Installing:

**Before:**
- [x] Assuming you already got a virtual environment for the project, active it: [/python/3-virtual-environment/activate-and-deactivate](/python/3-virtual-environment/activate-and-deactivate.md)

**1.1) Installing the tool:**
- [x] Install the DjLint as development dependency:

Using UV:
```bash
uv add --group dev djlint
```
Check if everything's right on the project's `pyproject.toml` file!

Or using PIP:
```bash
python3 -m pip install -U djlint
```
Only for non-UV user, add this dependency as a dev one in `pyproject.toml`:
```toml
# App-level Non-Core Dependencies:
[dependency-groups]
dev = [
	# ...
	"djlint>=1.46.4",  # Make sure this is the minimum version you need. You can pin exactly what version you wanna with == or a range.
]
```

---
## 2) Integration:

- [x] 2.1) Still in `pyproject.toml` file, add these lines:
```toml
# Django template Linter and Formatter:
[tool.djlint]
profile="django"
max_line_length = 100
preserve_blank_lines = true
close_void_tags = true
```
If this project is using [Prettier](/javascript/linter-formatter-typechecker/prettier/_about.md) or other CSS/JS formatter:
```toml
format_css = false  # false = Prettier should take care of it!
format_js = false  # false = Prettier should take care of it!
```

- [x] 2.2) And manually install the DjLint extension for your Code IDE.

- [x] 2.3) DjLint configuration on IDE:

Using VSCode:
1. Assuming you already have: [/python/web-development/django/ide/vscode/examples/.vscode/settings.json](/python/web-development/django/ide/vscode/examples/.vscode/settings.json)
2. In `/project/.vscode/settings.json`, add the lines:
```json
// PYTHON SETTINGS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
...
// DJANGO SETTINGS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
...
"[django-html]": {
	"editor.defaultFormatter": "monosans.djlint", // DjLint
	...
},
```

---

