

DJANGO SUB-APPS: MOVING AN APP

    Let's imagine this project structure:
        /your_project_django/core/
        /your_project_django/myapp/
    
    In case you want to move the /myapp/ to a new folder '/apps/', do it:

        
        >> /core/settings.py:

            In the INSTALLED_APPS array:

            from: "pagex"
            to:   "apps.pagex"


        >> /myapp/apps.py:

            From: name = 'pagex'
            To:   name = 'apps.pagex' # case the sub-folder is called 'apps'.

            E.g.
                class PagexConfig(AppConfig):
                default_auto_field = 'django.db.models.BigAutoField'
                name = 'apps.pagex'