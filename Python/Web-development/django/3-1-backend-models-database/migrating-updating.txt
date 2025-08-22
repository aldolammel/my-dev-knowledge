

MODELS.PY: UPDATING SOMETHING

    If you performe any modification in a models.py file, you must execute a migration again
            
        1) Make Django translate to SQL instruction all you need to do in the database:
        
            1A) For all sub-apps in the same time;
            1B) Or for a specific one;

            - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

            1A) For all apps:

                $ python manage.py makemigrations
                # or 
                $ uv run manage.py makemigrations

            1B) Or for a specific one:
            
                $ python manage.py makemigrations <subapp_name>
                # or 
                $ uv run manage.py makemigrations <subapp_name>

            - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        
        2) Check files in the sub-app migrations folder, and, if everything is okay, do it:
            $ python manage.py migrate
            # or 
            $ uv run manage.py migrate