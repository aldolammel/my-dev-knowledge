### Python > Django > Forms
# Error messages

---
## Learn the basic:
- Basic validations: [python/web-development/django/6-errors-and-validations/1-validation-basic](python/web-development/django/6-errors-and-validations/1-validation-basic.md)
- Clean method: [python/web-development/django/6-errors-and-validations/2-clean-differences-between-model-and-form.py](python/web-development/django/6-errors-and-validations/2-clean-differences-between-model-and-form.py)
- Error messages itself: [python/web-development/django/6-errors-and-validations/3-error-messages](python/web-development/django/6-errors-and-validations/3-error-messages.md)

---
## Error messages on Django template:
- Form Error Messages: [python/web-development/django/3-3-frontend-templates/form-error-messages.html](python/web-development/django/3-3-frontend-templates/form-error-messages.html)
- Form Error CSS Customization: [python/web-development/django/3-3-frontend-templates/form-error-css-customization](python/web-development/django/3-3-frontend-templates/form-error-css-customization.md)

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

==WIP:==
## (WIP) Model argument 'error_messages={}' (server-side checking):

It's the most reliable and solid way to ensure that anything that causes an infraction for a given attribute will generate the planned error message. However, this method is server-side, that is, it's handled by the server and not by the client machine.

```
<example here> xxxxxxxxxxxxxxxx
```

---
## Error messages on App and CMS front-end (client-side checking):

It's a great way to validate fields without consuming server resources.

### Basic
- [python/web-development/django/6-errors-and-validations/validation-2-for-app-forms](python/web-development/django/6-errors-and-validations/validation-2-for-app-forms.md)
- [python/web-development/django/6-errors-and-validations/validation-3-for-CMS-forms](python/web-development/django/6-errors-and-validations/validation-3-for-CMS-forms.md)

### Knowledge regarding error message feedbacks via final user app's front-end
- **Using Django Template:** .../django/3-3-frontend-templates/form-error-messages.html
- **Using Vue:** /xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
- **Using React:** /xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
- **Using Angular:** /xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

---

## Django Admin > Adding an extra feedback message in a detail-view:

[python/web-development/django/4-cms-admin/1-customizing/detailview-including-extra-text-messages.py](python/web-development/django/4-cms-admin/1-customizing/detailview-including-extra-text-messages.py)

