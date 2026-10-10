#### Python > Linter, Formatter & Type checkers > Ruff
# Checking and fixing errors

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

