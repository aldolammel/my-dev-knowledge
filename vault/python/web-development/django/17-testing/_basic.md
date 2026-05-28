

DJANGO > TESTING


    >> As soon the back-end is solid for real testing:

        >> Execute Django without reloads:

            This approach avoids Django to close unexpectedly during the tests:
            
                $ python manage.py runserver
                or 
                $ uv run manage.py runserver --noreload


    >> How to create Django tests:

        xxxxxxxxxxxxxxxx