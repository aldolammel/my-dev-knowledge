E.g., `/frontend/.env` file:
```python
# REMEMBER:
# .ENV FILES ONLY FOR DEVELOPMENT/STAGING ENVIRONMENTS! NEVER IN PRODUCTION!

# FRONTEND SETTINGS:
# ATTENTION: replace 'FRONT_' for 'VITE_' if you're using Vue with Vite build-tool.

# CRITICAL WHEN USING VITE:
# 1. Environment vars demanding 'VITE_' prefix.
# 2. These vars are exposed to client-side code, so NEVER put secrets, credentials, or tokens!

FRONT_DEBUG=true
#VITE_DEBUG=true

# Don't use the trailing slash!
FRONT_PROD_BASE_URL=https://product-main-domain.com
#VITE_PROD_BASE_URL=https://product-main-domain.com

# Under Production, replace it by VITE_PROD_BASE_URL value!
#VITE_BASE_URL=http://localhost:8000
#VITE_ROUTER_BASE=/
```