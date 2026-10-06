#### Python > Package Manager > UV
# `uv lock` command

---

==Critical to understand:==
Once the [pyproject.toml](/python/web-development/pyproject.md) declares what the project needs, the `uv.lock` file (automatically created by [uv init](/python/package-manager/uv/uv-init.md) command) records exactly what was resolved/installed into the `.venv` folder. It's crucial to have `uv.lock` file synced with `pyproject.toml` file, so every version adjusted in there must be followed by running `uv sync` in order to get the `uv.lock` file and `.venv` folder updated!

---
## Try to use `uv sync`, not `uv lock`
Basically, 99% of your time updating `pyproject.toml` (using `uv add` or `uv remove` commands or version limitations manually) will be through the [uv sync](/python/package-manager/uv/auto-installation-with-sync.md) command once `uv sync` is more useful generally. 

|                                               | `uv lock` | `uv sync` |
| --------------------------------------------- | --------- | --------- |
| Updates `uv.lock` if `pyproject.toml` changed | Yes       | Yes       |
| Installs/removes packages in `.venv`          | No        | Yes       |
| Creates `.venv` if missing                    | No        | Yes       |

---
## When it can be a better choice (Advanced):
In case you wanna update the `uv.lock` file but NOT the `.venv` folder (for special reasons), you would use `uv lock` command. 