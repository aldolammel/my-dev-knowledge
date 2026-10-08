#### Python > Package Manager > UV
# Auto-installation

---

==Critical / On Prod:==
Read this in case you wanna do it on [Prod](/dev-concepts/environment-production-prod.md): [/python/package-manager/uv/production-with-uv](/python/package-manager/uv/production-with-uv.md)

---

**In case your project just has a `requirements.txt`:** 
- Convert your current existing project using `requirements.txt` to use `pyproject.toml` file: [/python/package-manager/uv/converting-non-uv-project-in-one](/python/package-manager/uv/converting-non-uv-project-in-one.md)

---
## 1) Make a choice:

- 1A) I'm updating Python in a project.
- 1B) I'm updating `pyproject.toml` dependency version limitations.
- 1C) I lost the virtual environment folder in a project.
- 1D) I just cloned an existing project repo.
- 1E) Something wrong with my project dependencies.

......................................
### 1A) I'm updating Python in a project

- [ ] **Before:**
	1. Assuming you manually pinned the new Python version through UV (like you should have updated the `.python-version` file): [/python/package-manager/uv/pin-python-version](/python/package-manager/uv/pin-python-version.md)
	2. Assuming you manually updated the Python version in the `pyproject.toml`.

- [ ] **A1.1) Syncing**: [uv sync command](/python/package-manager/uv/uv-sync.md)

......................................
### 1B) I'm updating `pyproject.toml` dependency version limitations

Case you went to that file and updated one or more dependency version, you need to re-sync for make the uv.lock file and the .venv folder get updated if needed. So, in your project folder/environment, do the A1 steps!

......................................
### 1C) I lost the virtual environment folder in a project

In this case you need to re-create the `.venv` folder based in what your `pyproject.toml` file is describing. So, in your project folder/environment, do the A1 steps!

......................................
### 1D) I just cloned an existing project repo

Once you have no any `.venv` created for this project yet (at least it should be available in a repository), in your project folder/environment, do the A1 steps!

......................................
### 1E) Something wrong with my project dependencies

In this scenario, the first thing to know is to check your `pyproject.toml` file still in the project root folder. If not, you should read about [uv init command](/python/package-manager/uv/uv-init.md) and, then, about the [uv sync command](/python/package-manager/uv/uv-sync.md).

---
