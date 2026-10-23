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

- [ ] 2.2) (If applicable) If your project is using `pyproject.toml` instead of `requirements-dev.txt`, include these configures in there:
```toml
# This file is a model of Ruff configuration in pyproject.toml

# App-level Non-Core Dependencies:
[dependency-groups]
dev = [
    # ...
    "ruff>=0.16.10",
]

# Python Linter and Formatter:
[tool.ruff]
line-length = 100
indent-width = 4
target-version = "py313"  # Python version (py313 means newest of 3.13 = 3.13.9) <------------------

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false  # e.g. that comma right after the last element of an array.
line-ending = "auto"  # automatically detect the appropriate line ending.
docstring-code-format = true
docstring-code-line-length = "dynamic"

[tool.ruff.lint]
# Enable Pyflakes (`F`) and a subset of the pycodestyle (`E`) codes by default. Unlike Flake8, Ruff
# doesn't enable pycodestyle warnings (`W`) or McCabe complexity (`C901`) by default:
select = [
    "DJ",  # Django-specific rules
    "E4",  # pycodestyle errors
    "E7",
    "E9",
    "W",  # pycodestyle warnings
    # "F",  # Pyflakes, detects and delete imported modules or names that are not used.
    "I",  # isort
    "N",  # pep8-naming
    "Q",  # flake8-quotes.
    #"UP",  # pyupgrade - automatically upgrade syntax for newer Python versions
    "B",  # flake8-bugbear - find likely bugs and design problems
    "C4",  # flake8-comprehensions - better list/set/dict comprehensions
    "SIM",  # flake8-simplify - simplify code
]
ignore = [
    "DJ001",  # Avoid using null=True on string-based fields
    "DJ007",  # Avoid to use fields = "__all__", preferring to list array with fields.
    "E501",  # Line too long (handled by formatter)
    "B904",  # Within an `except` clause, raise exceptions with `raise ... from err`
]
fixable = ["ALL"]  # Allow fix for all enabled rules (when `--fix`) is provided.
unfixable = [
    "B",  # Avoid trying to fix flake8-bugbear (`B`) violations.
]
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"  # Allow unused variables when underscore-prefixed.
[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["E402"]
"**/{tests,docs,tools}/*" = ["E402"]
"**/migrations/*" = ["E501", "DJ001"]  # Migrations can have long lines and null=True
"**/settings/*" = ["F405"]  # Allow star imports in settings
[tool.ruff.lint.flake8-quotes]
docstring-quotes = "double"
```

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

- [ ] 2.5) (Optional) Run the checking and fixing for the first time: [/python/linter-formatter-typechecker/ruff/checking-and-fixing-errors](/python/linter-formatter-typechecker/ruff/checking-and-fixing-errors.md)

---

