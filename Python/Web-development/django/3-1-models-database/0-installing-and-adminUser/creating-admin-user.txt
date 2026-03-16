

CREATING THE SUPER ADMIN USER:


    PRE) After to install the desired database:
        ./_define-the-database.txt


    1) Let's perform the database basic tasks:
        # It creates the database with basic tables:
            $ python manage.py migrate
        #or
            $ uv run manage.py migrate


    2) Creating the admin user:
        $ python manage.py createsuperuser
        #or
        $ uv run manage.py createsuperuser
        
        # Now, try to login, making sure the application is running:
        http://localhost:8000/admin/