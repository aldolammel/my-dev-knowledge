#### Python > Linter, Formatter & Type checkers
# Ruff

---

Ruff is a high-performance linter and code formatter for Python, developed by Astral. It's notable for its exceptional speed, largely attributed to being written in Rust. 

**If checks:**
- Python syntax errors.
- Import sorting.
- Code style (PEP 8).
- Bugs.
- Complexity.
- Etc.

TIP: Ruff is developed by the same company of the UV Package manager, so both are completely integrated: [/python/package-manager/uv/\_about-install-and-update](/python/package-manager/uv/_about-install-and-update.md)

---
## Installation & Integration:
[installation](/python/linter-formatter-typechecker/ruff/installation.md)

---
    
HOW TO CHECK CODE ERRORS:
```bash
uv run ruff check
```

HOW TO FIX CODE ERRORS AUTOMATICALLY:
```bash
uv run ruff check --fix
```

HOW TO FIX CODE FORMATTING:
```bash
uv run ruff format                      # Format all files in project-folder (except files like .venv/, dist/, build/, .vscode/, .git/, etc).
uv run ruff format path/to/code/        # Format all files in `path/to/code` (and any subdirectories).
uv run ruff format path/to/file.py      # Format a single file.
```

---
