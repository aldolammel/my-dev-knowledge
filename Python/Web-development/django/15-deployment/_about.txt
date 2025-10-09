
    DJANGO ABOUT DEPLOYMENT:
        # Check the documentation version after get into:
        https://docs.djangoproject.com/en/5.2/howto/deployment/
    
    
    UDEMY:
        https://www.udemy.com/course/python-django-the-practical-guide/learn/lecture/26399466




    x) 


    x) 


    x) 



    x) Run the collectstatic command to create automatically the 'staticfiles' in your
        project folder:

            $ python manage.py collectstatic

            This command will copy all static files (including the Django admin CSS) into the 
            staticfiles directory (STATIC_ROOT).

            Since DEBUG=False, Django relies on the web server to serve static files, and you must 
            ensure all static files (including admin CSS) are collected into the STATIC_ROOT 
            directory by running collecstatic command already shown above.

            The very first time to run the collectstatic command in a Django project is typically
            just before deploying your project to a production environment. This is when you need to
            gather all static files from the various apps and locations into a single directory that
            can be easily served by your web server (such as Nginx or Apache).