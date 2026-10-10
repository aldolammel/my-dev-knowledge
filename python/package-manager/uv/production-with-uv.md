#### Python > Package manger > UV
# Safe approach on production with UV

---

**Before:**

1. What is Production: [/dev-concepts/environment-production-prod](/dev-concepts/environment-production-prod.md)

Deploy script on the VPS should consider it. Put it in the deploy script, CI config, *Dockerfile* or *Makefile*, so it lives with the project:
```bash
uv sync --group prod --locked --no-dev
# --group prod = install all core and prod dependencies.
# --locked = fails if `uv.lock` doesn’t match `pyproject.toml`, instead of silently updating the lockfile.
# --no-dev = skips the dev group in production, which you'll want there.
```

---
## Deploy on Prod with Django:
[/python/web-development/django/15-deployment/\_about](/python/web-development/django/15-deployment/_about.md)
