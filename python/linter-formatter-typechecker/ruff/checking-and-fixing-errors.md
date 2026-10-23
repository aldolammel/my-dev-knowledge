#### Python > Linter, Formatter & Type checkers > Ruff
# Checking and fixing errors

---
## Checking code errors (lint):
```bash
# General scan:
uv run ruff check
# Or only in a specific folder:
uv run ruff check apps/subapp_name/
# Or only in a specific file:
uv run ruff check apps/subapp_name/models.py
```
## Automatic fixing (lint):
Just include the flag `--fix`.
```bash
# General fix:
uv run ruff check --fix
# Or only in a specific folder:
uv run ruff check apps/subapp_name/ --fix
# Or only in a specific file:
uv run ruff check apps/subapp_name/models.py --fix
```
## Only focusing in to be formatter:
```bash
uv run ruff format                             # Format all files in project-folder (except files like .venv/, dist/, build/, .vscode/, .git/, etc).
uv run ruff format apps/subapp_name/           # Format all folder content.
uv run ruff format apps/subapp_name/models.py  # Format a single file.
```

