#### Environment Variables
# Back-end `.env` file

---
## Before:
- Remember: `.env` file ==NEVER== in [prod](/dev-concepts/environment-production-prod.md) environment!

---

```python
# REMEMBER: NEVER USE THIS FILE IN PRODUCTION, EVEN IN A REPO!
# BACKEND SETTINGS:
DEBUG=True
ALLOWED_HOSTS=.exampledomain.com,localhost,127.0.0.1
# Don't use the trailing slash!
PROD_BASE_URL=https://exampledomain.com
# Don't use the trailing slash!
BACK_URL1=http://localhost:8000
# Don't use the trailing slash!
BACK_URL2=http://127.0.0.1:8000
# Don't use the trailing slash!
#FRONT_URL1=http://localhost:5173
# Don't use the trailing slash!
#FRONT_URL2=http://127.0.0.1:5173
# DATABASE SETTINGS:
# postgres default postgres
DATABASE_NAME=your_db_name
# postgres default postgres
DATABASE_USER=your_db_user
# postgres default postgres
DATABASE_PASSWORD=your_db_password
# postgres default localhost
DATABASE_HOST=your_db_host
# postgres default 5432
DATABASE_PORT=your_db_port
# EMAIL SETTINGS:
# ...
```
### For Emails using Gmail
```python
# ...
# EMAIL SETTINGS:
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=emailproject@gmail.com
# https://myaccount.google.com/apppasswords
EMAIL_HOST_PASSWORD=password_generated_here
DEFAULT_FROM_EMAIL=emailproject@gmail.com
```
Generating password by Gmail:
1. https://myaccount.google.com/apppasswords or `Google Account -> Security -> 2-Step Verification -> App Passwords -> Select App -> Generate`
2. If `App Passwords` option is not available, make sure you have enabled  `2-Step Verification is enabled`.
3. After that, go to Security home and, through the search bar, search for `App Passwords`.

---
## In addition, settings based on language and framework:

**For Python/Django:**
- Secret Key: [/python/web-development/django/1-install-and-first-steps/secret-key](/python/web-development/django/1-install-and-first-steps/secret-key.md) 
- Email settings: [/python/web-development/django/13-email/config-settings](/python/web-development/django/13-email/config-settings.md)

---
## You can use it in these environments:
 - [Development](/dev-concepts/environment-development-dev.md)
 - [Testing (QA)](/dev-concepts/environment-testing-qa.md)
 - [Staging (UAT)](/dev-concepts/environment-staging-uat.md)! Yes, you can!

---

