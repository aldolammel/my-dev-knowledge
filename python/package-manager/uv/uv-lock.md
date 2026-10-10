#### Python > Package Manager > UV
# `uv lock` command

---

==Critical to understand:==
The `uv lock` command exists to be used after the [pyproject.toml](python/pyproject-toml.md) manual edition by a developer. The command edits the `uv.lock` file (automatically created by [uv init command](/python/package-manager/uv/uv-init.md)) without to change what is installed in `.venv` folder, unlike [uv sync command](/python/package-manager/uv/uv-sync.md) that update the `uv.lock` file and the `.venv` folder.

---
## Try to use `uv sync`, not `uv lock`
Basically, 99% of your time updating `pyproject.toml` (using `uv add` or `uv remove` commands or version limitations manually) will be through the [uv sync](/python/package-manager/uv/uv-sync.md) command once `uv sync` is more useful generally. 

|                                               | `uv lock` | `uv sync` |
| --------------------------------------------- | --------- | --------- |
| Updates `uv.lock` if `pyproject.toml` changed | Yes       | Yes       |
| Installs/removes packages in `.venv`          | No        | Yes       |
| Creates `.venv` if missing                    | No        | Yes       |

---
## What `uv lock` with `--check` flag do: 
It verifies that `uv.lock` matches the dependency requirements declared in `pyproject.toml`:
```bash
uv lock --check
```

---
## When it can be a better choice (Advanced):
In case you wanna update the `uv.lock` file but NOT the `.venv` folder (for special reasons), you would use only `uv lock` command, never `uv sync`.