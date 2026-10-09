#### Python > Django > Translate & Internationalization
# Translate with dynamic composition

---

You can build smart translations for all types of sentence through any language using dynamic compositions with [Parler module](/python/web-development/django/component-libraries/django-parler/0-django-parler.md).

E.g. in `/core/consts.py`:
More about: [/python/web-development/django/3-1-models-database/\_constants-map](/python/web-development/django/3-1-models-database/_constants-map.md)
```python
VAL_PROFILE_NAME_MAXLNGH = 20
```

E.g. in `/core/lang.py`:
More about: [/python/web-development/django/8-translate-and-internationalization/language-file-example.py](/python/web-development/django/8-translate-and-internationalization/language-file-example.py)
```python
LB_PROFILE_NAME = _('Profile Name')
TX_ERRO_PROFILE_NAME_MAXLNGH = _('%(txt)s cannot exceed %(val)s characters.')
```

E.g. in `/apps/subapp/models.py`:
```python
from core import consts, lang

class Profile(models.ModelForm):
	name = models.CharField(
		max_length=consts.VAL_PROFILE_NAME_MAXLNGH,
		verbose_name = lang.LB_PROFILE_NAME,
		error_messages={
			'max_length': lang.TX_ERRO_PROFILE_NAME_MAXLNGH % {
				'txt': lang.LB_PROFILE_NAME,
				'val': consts.VAL_PROFILE_NAME_MAXLNGH,
			},
		},
	)
```

==WARNING:==
Unfortunately, you cannot make all translations directly on the `/core/lang.py` file. If you use at same time a translatable variable that will feed another translatable variable (dynamic composition), [Parler](/python/web-development/django/component-libraries/django-parler/0-django-parler.md) badly tries to translate everything at the same time, bringing weird behaviors, some times translating to a wrong language, even making the `makemigrations` command performs unwanted changes.
```python
# Never do this (directly using `gettext_lazy` aside):
TX_ERRO_PROFILE_NAME_MAXLNGH = _('%(txt)s cannot exceed %(val)s characters.') % {
	'txt': lng.LB_PROFILE_NAME,
	'val': VAL_PROFILE_NAME_MAXLNGH,
},
```

---
## Avoid Circular Errors:
[/python/web-development/django/6-errors-and-validations/importing-no-circular](/python/web-development/django/6-errors-and-validations/importing-no-circular.md)

