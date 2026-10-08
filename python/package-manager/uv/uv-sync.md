#### Python > Package Manager > UV
# `uv sync` command

---

The `uv sync` command looks for project `pyproject.toml` file to listing the configurations and dependencies and, if something changed in the `pyproject.toml`, the command will update the `uv.lock` file and the `.venv` folder.

**Command scope:**
- `uv.lock` is the central file, and UV manages it, so you shouldn't edit `uv.lock` (*lockfile*) by hand.
- It does re-lock automatically if `pyproject.toml` changed (for example, you added or edited a dependency).
- It compares the *lockfile* against what's in your `.venv` and installs, removes or changes only what differs. By default the sync is exact, so packages not in the lock get removed.

---
## Before:

1. Assuming you are in the project root folder (not need to be activated in the project venv)!
2. Assuming that this project root folder has a `.venv`, a `pyproject.toml`, and a `uv.lock`. If not, read it: [uv init](/python/package-manager/uv/uv-init.md)

---
## 1) Syncing, make a choice:

==Critical:==
In [Production environments](dev-concepts/environment-production-prod.md), you should NEVER synchronize any development dependencies!

**Option 1:** Core dependencies and all dependencies from development sub-group:
```bash
uv sync --extra dev
```

**Option 2:** Only the core dependencies:
```bash
uv sync
```

**Option 3:** Core dependencies, including multiples sub-groups of dependencies:
```bash
uv sync --extra dev --extra test
```

---
## 2) (Optional) Check the `uv.lock` file:

```bash
uv lock --check  # Optional 'cuz, after the sync command, it's almost impossible any issue in 'uv.lock' file.
```

---
