#### Python > Package Manager > UV
# New project using UV

---

**Make one more choice:**
- 1A) Create a project with `pyproject.toml` dependencies and tools control.
- 1B) I just need the `venv` and nothing else.

......................................

**1A) Create a project with `pyproject.toml` dependencies and tools control, and Git repository-ready:**

Create the minimal Python project scaffolding. It creates automatically some files like `pyproject.toml`. Don't use this for existing projects with these files already:
```bash
uv init
```
And then create the venv:
```bash
uv venv
```

......................................

**1B) I just need the `venv` and nothing else:**
```bash
uv venv
```
