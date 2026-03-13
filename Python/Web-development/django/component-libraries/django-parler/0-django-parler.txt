

DJANGO LIB: DJANGO-PARLER:

    Django-Parler is a third-party application for Django that provides a clean, flexible way to add multilingual content to your Django models. It allows you to translate specific fields in your database models, manage those translations in the admin interface, and retrieve content in the appropriate language automatically.


    1) Installation:

        # Using UV:
            $ uv add django-parler
        
        # Or using PIP:
            $ python3 -m pip install django-parler


    2) Integration:

        2.1) In core/settings.py:
            
            Installed_Apps:
                # THIRD-PARTY SUB-APPS:
                “parler”,

        2.1) Still through settings.py, add in 'Internationalization' section:

                #PARLER_DEFAULT_LANGUAGE_CODE = LANGUAGE_CODE  # Not needed because 'fallbacks' is set manually.
                PARLER_LANGUAGES = {
                    None: (
                        {'code': LANG_CODE_PTBR},
                        {'code': LANG_CODE_ES},
                        {'code': LANG_CODE_ENUS},
                    ),
                    'default': {
                        'fallbacks': [LANG_CODE_ENUS, LANG_CODE_PTBR],  # Cascade fallbacks!
                        'hide_untranslated': False,
                    },
                }

                >> For multi-site project: replace None with the SITE_ID. Each SITE_ID can be added
                    as additional entry in the dictionary.

        2.2) Check these instructions:
            .../django/8-translate-and-internationalization/1-starting-translation.txt