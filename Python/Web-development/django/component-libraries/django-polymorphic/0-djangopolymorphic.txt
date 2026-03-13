

DJANGO > POLYMORPHIC SOLUTION: DJANGO-POLYMORPHIC


    It's builds on top of the standard Django model inheritance. It makes using inherited models easier. When a query is made at the base model, the inherited model classes are returned.

    https://django-polymorphic.readthedocs.io/en/latest/
    

    >> Examples:
        ./example/basic.py
        ./example/real-case.py
        
    
    >> INSTALLING:

        PRE) Assuming you already are in the project environment!

        1) Install as a project dependency:
            
            LINUX:
                # PIP:
                    $ pip install django-polymorphic
                # Or UV:
                    $ uv add django-polymorphic

            WINDOWS:
                $ xxxxxxxxxxxxxxxxxxxxx


    >> INTEGRATING:

        1) In your Django core settings:

            INSTALLED_APPS = [
                # DJANGO DEFAULT SUB-APPS:
                'django.contrib.contenttypes',
                # THIRD-PARTY SUB-APPS:
                'polymorphic',
            ]


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


    EXAMPLES:
        ./example/basic.py
        ./example/real-case.py


    

