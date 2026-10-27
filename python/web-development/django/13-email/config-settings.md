#### Python > Django > E-email
# Configuring e-mail service in Django

---
## 1) In `settings.py`:
```python
# ...

# Email settings:
EMAIL_BACKEND = env('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env('EMAIL_USE_TLS', default=True)
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
```

---
## 2) Update your `.env` file:
```python
# ...

# EMAIL SETTINGS:
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
# ...
# Include this note in there: Other e-mails can be listed in /core/consts.py!
```
Model of local back-end .env: [env](/environment-variables/env-for-local/in-backend/env.md)

---
## In `/core/consts.py:`
Sometimes can exist more emails to list or listed in here: `/core/consts.py`!

---


