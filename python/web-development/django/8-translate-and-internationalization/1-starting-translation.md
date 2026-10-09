#### Python > Django > Translate & Internationalization
# Starting to translate

---
## 1) Setup the internationalization project:

- [x] 1.1) Install basic modules:
	- (Server level) Gettext (to translate the content itself): [/web-development/components-libraries-server-level/gettext/0-gettext](/web-development/components-libraries-server-level/gettext/0-gettext.md)
	- (App level) Rosetta app (include an admin sub-app to manage translations): [/python/web-development/django/component-libraries/django-rosetta/0-django-rosetta](/python/web-development/django/component-libraries/django-rosetta/0-django-rosetta.md)

- [x] 1.2) In `settings.py`, add the `LocaleMiddleware` between `Session` and `Common` middlewares:
```python
MIDDLEWARE = [
	"django.contrib.sessions.middleware.SessionMiddleware",
	"django.middleware.locale.LocaleMiddleware",  # Django additional feature!
	"django.middleware.common.CommonMiddleware",
]
```

==Crucial:== middleware order matters! So double-check with these guidelines:
- Make sure it’s one of the first middleware installed.
- It should come after `SessionMiddleware`, because `LocaleMiddleware` makes use of session data.
- It should come before `CommonMiddleware` because `CommonMiddleware` needs an activated language in order to resolve the requested URL.
- If you use `CacheMiddleware`, put `LocaleMiddleware` after it;

- [x] 1.3) Still in `settings.py`, in `internationalization` section:
```python
# Internationalization
USE_I18N = True  # 'True' for multi-language support!
# Available languages:
LANG_CODE_PT = "pt"
# LANG_CODE_PTBR = "pt-br"  # In case it will be a big translation projects, maybe it's better to use specific language codes!
LANG_CODE_ES = "es"
# LANG_CODE_ESMX = "es-mx"  # In case it will be a big translation projects, maybe it's better to use specific language codes!
LANG_CODE_EN = "en"
# LANG_CODE_ENUS = "en-us"  # In case it will be a big translation projects, maybe it's better to use specific language codes!
LANGUAGES = [
	(LANG_CODE_PT, 'Português (PT)'),
	(LANG_CODE_ES, 'Español (ES)'),
	(LANG_CODE_EN, 'English (US)'),
]
# App default language:
LANGUAGE_CODE = LANG_CODE_PT
LOCALE_PATHS = [BASE_DIR / 'locale']
LANGUAGE_COOKIE_NAME = 'user_language'
LANGUAGE_COOKIE_AGE = 2592000  # 30 days.

# Timezone-aware
USE_TZ = True  # 'True' for multi-language support compatibility!
TIME_ZONE = 'America/Sao_Paulo'  # 'UTC'

# FORMATS
# Date:
DATE_FORMAT = 'Y-m-d'  # ISO format for dates ('2006-10-25')
SHORT_DATE_FORMAT = 'd-m-Y'  # '25-10-2006'
# Time:
TIME_FORMAT = 'H:i'  # 24-hour format (H): '14:30'
# Datetime:
DATETIME_FORMAT = f'{DATE_FORMAT} {TIME_FORMAT}'  # '2006-10-25 14:30'
DATETIME_INPUT_FORMATS = [
	'%Y-%m-%d %H:%M',  # '2006-10-25 14:30'
	'%Y/%m/%d %H:%M',  # '2006/10/25 14:30'
]
# Input formats:
DATE_INPUT_FORMATS = [
	'%Y-%m-%d',  # ISO 'yyyy-mm-dd'
	'%d/%m/%Y',  # '25/10/2006'
	'%d-%m-%Y',  # '25-10-2006'
]
TIME_INPUT_FORMATS = [
	'%H:%M',  # '14:30'
	'%H%M',  # '1430'
]
# Others:
FIRST_DAY_OF_WEEK = 1  # 0 = Sunday
```

- [x] 1.4) Still in the core folder, edit the main `core/urls.py` file:
```python
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

# DJANGO BASIC:
urlpatterns = i18n_patterns(
	# CMS:
	path('admin/', admin.site.urls),
	# SUB-APPs, APIs:
	# ...
	path('rosetta/', include('rosetta.urls')),  # Keep it like that (without 'apps.'), even you're using an apps package folder.
)
```

- [x] 1.5) (Optional) If you want your URL's, if through default language, without the language prefix, do this:
```python
urlpatterns = i18n_patterns(
	# ...,
	# ...,
	# ...,
	prefix_default_language=False,
)
```
==Be aware:== maybe for advanced language settings, you'll need to use it as True!

- [x] 1.6) (Optional) Create the `/core/lang.py` file:
	- [/python/web-development/django/8-translate-and-internationalization/language-file-example.py](/python/web-development/django/8-translate-and-internationalization/language-file-example.py)
	- [/python/web-development/django/8-translate-and-internationalization/translate-dynamic-compositions](/python/web-development/django/8-translate-and-internationalization/translate-dynamic-compositions.md)

- [x] 1.7) (If applicable / Optional) IDE configs, on the VSCode, set this in the project `.vscode/settings.json` file:
```json
// DJANGO SETTINGS
"django.i18n": true, // Activates the i18n features for snippets (eg.: _(""))
// ...
```

---

## ==Weight if you should keep going in the current development phase:==
Don't invest more time with the below steps once your project just started. It could be safer and better only to go to the next steps of this roadmap after you got a good development evolution of your project. If you have it, keep going, otherwise, return to the roadmap that brings you here. Further other roadmaps will remember to call you to check this steps again.

---
## 2) Defining which text-contents are translatable:

- [ ] 2.1) Method to translate Views and Models:
```python
from django.utils.translation import gettext_lazy as _  # This '_' is a convention!

class Product(models.Model):
	name = models.CharField(
		verbose_name=_("Product Name"),
		...
	)
	description = models.TextField(
		verbose_name=_("Description"),
		...
	)
```

==CRUCIAL:== After translate your models, remember to run `makemigrations` and `migrate` commands.

- [ ] 2.2) Method to translate Templates:

Call this in the FIRST line on each html file that's using translation benefits, EXCEPT if the template is calling the template-tag 'extends':
```html
{% extends "base.html" %}     <!-- Always the first line! -->
{% load i18n %}
```

==Crucial:== 
The 'load' must be called even in 'includes'.

Translating the HTML content itself:
```html
<h1>{% trans "Welcome" %}</h1>
<p>{% trans "I am Aldo Lammel" %}.</p>
```

Sometimes you can easy translate the text directly in the View, sending the translate to template through Context. It's up to you.

- [ ] 2.3) Finishing the definition process:

                >> Don't worry about future updates over the translatable content.
                    Later, I'll show how-to.

                >> In project-root, create a folder called 'locale';

                >> Create in 'locale' folder the sub-folders for each additional language needed:

                    E.g.

                        /en/ or /en_US/
                        /pt/ or /pt_BR/
                        /es/

                        >> Be carefull because <html lang="THIS_ATTRIBUTE"> accepts only 2 characters!

Create all language files (`.PO`):
```bash
django-admin makemessages --all
```
Or, if you are using UV:
```bash
uv run manage.py makemessages --all
```

Gettext Module automatically will set each .PO file in the right folder.

---
## 3) Non-database Translation process:

- [ ] 3.1) Default language:

If your project's product is written in English, probably the default language declared in `settings.py` is 'en' or some variant of that. That said, you can leave the `/en/django.po` file untouchable 'cause Gettext will assume each empty 'msgstr' means each 'msgid' text is the default/original one;

- [ ] 3.2) Additional language:

                >> In some additional language folder, e.g. /locale/pt_BR/,
                    edit the 'django.po' file (not-recommended):

                        E.g.

                            msgid "Welcome"
                            msgstr "Bem-vindo(a)"

                            msgid "I am Aldo Lammel"
                            msgstr "Me chamo Aldo Lammel"

                >> TIP: after to understand how a .po file works, it's advised to use Rosetta Module
                    to work on a translation (recommended):

                        http://localhost:8000/rosetta/


- [ ] 3.3) For all or just one (it don't matter) language: once you've translated the strings in some `.po` file, you should to compile that/them:

Using UV:
```bash
uv run manage.py compilemessages
```
Or Django solution:
```bash
django-admin compilemessages
```

- [ ] 3.4) To test results:

E.g.
http://localhost:8000/en/
http://localhost:8000/pt-br/
http://localhost:8000/es/

---
## 4) Database Translation process:

- [ ] 4.1) Install and integrate Parler Module: [/python/web-development/django/component-libraries/django-parler/0-django-parler](/python/web-development/django/component-libraries/django-parler/0-django-parler.md)

- [ ] 4.2) For Models: [/python/web-development/django/8-translate-and-internationalization/translate-models](/python/web-development/django/8-translate-and-internationalization/translate-models.md)

- [ ] 4.3) For CMS, through each sub-app admin.py file that has its models.py involved: [/python/web-development/django/8-translate-and-internationalization/translate-cms](/python/web-development/django/8-translate-and-internationalization/translate-cms.md)

- [ ] 4.4) For Model Managers and Model QuerySets: [/python/web-development/django/8-translate-and-internationalization/translate-querysets-and-managers](/python/web-development/django/8-translate-and-internationalization/translate-querysets-and-managers.md)

---
## 5) Language switching on the interface:

- [ ] 5.1) Create a global-context file called `context_processors.py` in 'general' sub-app:
```python
from django.conf import settings

def languages(request):
	"""Add LANGUAGES and current LANGUAGE_CODE to the context globally."""
	return {
		'LANGUAGES': settings.LANGUAGES,  # Available languages!
		'LANGUAGE_CODE': request.LANGUAGE_CODE,  # Currently active language!
	}
```

- [ ] 5.2) In `settings.py`, include that new global-context:
```python
TEMPLATES = [
	{
		# ...
		'OPTIONS': {
			'context_processors': [
				# DJANGO DEFAULT GLOBAL CONTEXTS:
				# ...
				# DJANGO ADDITIONAL GLOBAL CONTEXTS:
				# ...
				'general.context_processors.languages',  # <-------- add this!
				# THIRD-PARTY GLOBAL CONTEXTS:
				# Reserved space...
			],
		},
	},
]
```

- [ ] 5.3) On `/core/urls.py` file:
```python
# DJANGO:
path('i18n/', include('django.conf.urls.i18n')), # set_language view for lang change request.
```

This will enable Django's `set_language` view, which processes the language change request.

- [ ] 5.4) On your `base.html` template:

E.g.
```html
<html lang="{{ LANGUAGE_CODE }}">
```

To use a template-variable "{{ }}" globally:

**Using Pagex**, look for "Structure Content": [/python/web-development/django/useful-sub-apps/pagex/\_install-and-integration](/python/web-development/django/useful-sub-apps/pagex/_install-and-integration.md)

Or using Django native `/core/context_processors.py` solution: [/python/web-development/django/3-2-views-and-API/1-building-views-context/global-context](/python/web-development/django/3-2-views-and-API/1-building-views-context/global-context.md)

- [ ] 5.5) Still on templates, a language-selector, language-switch: [/python/web-development/django/8-translate-and-internationalization/language-selector.html](/python/web-development/django/8-translate-and-internationalization/language-selector.html)

---
## 6) Final touch:

- [ ] 6.1) Check each translation to fix all 'fuzzy' flag that means the translation needs translator attention!

- [ ] 6.2) (I never needed) Database: If your database contains any content that will be translated, ensure your PostgreSQL database is set up with UTF-8 encoding, which is necessary for handling multi-language content.
```bash
psql -U yourusername -d yourdbname -c
```

---
