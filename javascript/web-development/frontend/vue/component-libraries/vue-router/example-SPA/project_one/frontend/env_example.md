#### JavaScript > Front-end > Vue > Components & Libraries > Vue Router
# Vue Router needs in `/frontend/.env`

---
## If using Vite as build-tool:
```python
# FRONTEND SETTINGS:
# ...
VITE_PROD_BASE_URL=https://client-main-domain.com

# Under Production, replace it by VITE_PROD_BASE_URL value!
VITE_BASE_URL=http://localhost:8000
VITE_ROUTER_BASE=/

# Vite automatically searches for VITE_ prefix env vars, and it's accessible via import.meta.env.env_var_here
```

---
## If using Vue-CLI as build-tool:
```python
# FRONTEND SETTINGS:
# ...
PROD_BASE_URL=https://client-main-domain.com

# Under Production, replace it by PROD_BASE_URL value!
BASE_URL=http://localhost:8000
ROUTER_BASE=/

# It's accessible via import.meta.env.env_var_here
```

---


