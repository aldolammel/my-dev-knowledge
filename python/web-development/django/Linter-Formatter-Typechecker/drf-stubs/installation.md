#### Python > Django > Linter, Formatter & Type checker
# Django Rest Framework (DRF) Stubs

---

From the same team of [Django-Stubs](/python/web-development/django/Linter-Formatter-Typechecker/django-stubs/_installation.md), DRF Stubs adds type information for [Django REST Framework](/python/web-development/django/component-libraries/django-rest-framework/0-restframewok.md), since DRF doesn't ship its own type hints.

**What it does on DRF:**

- Type hints for DRF's public API: serializers, viewsets, generic views, permissions, authentication, request/response objects, pagination, and so on.
- A [MyPy](/python/linter-formatter-typechecker/MyPy/_installation.md) plugin that handles DRF's dynamic behavior, so MyPy understands things like serializer fields and generic classes.
- Generic parameters on DRF classes, so MyPy can then tell what type `serializer.instance` or `self.get_queryset()` returns.

---
## 1) Installing:

Using UV:
```bash
uv add --optional dev "djangorestframework-stubs"
# Check the version:
uv pip show djangorestframework-stubs
```

Using PIP:
```bash
pip install "djangorestframework-stubs"
# Check the version:
pip show djangorestframework-stubs
```
## 2) Integration:

- [ ] (If applicable) Only for who's working with PIP as package installer/manager, and `pyproject.toml` file:
```toml
[project.optional-dependencies]
dev = [
	# ...
	"djangorestframework-stubs>=1.4.0", # Recommended to define with a newer version!
]
```

- [ ] (If applicable) For UV user, as well as for PIP one, add this plugin line manually on the `pyproject.toml` file:
```toml
# Python static type checker:
[tool.mypy]
# ...
plugins = [
	"mypy_django_plugin.main", # Keep it at first!
	# ...
	"mypy_drf_plugin.main", # Add this right before this one up here.
]
# ...
```

---

