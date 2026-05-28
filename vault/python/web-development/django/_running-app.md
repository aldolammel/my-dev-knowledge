

DJANGO: RUNNING AN APP


    PRE.1) Keep it in mind: this app is using local db or a cloud one? Case local, is the db service running properly?


    PRE.2) Assuming you're in the project folder on Terminal;


    PRE.3) Assuming you got the project's environment activated:
        /vault/python/3-virtual-environment/activate-and-deactivate.txt


    PRE.4) (If applicable)
        Assuming you're in the right Git branch;
            /vault/versioning/git/command-branch.txt
            /vault/versioning/git/command-checkout.txt
    

    4) Run the app:

        # Using UV:
            # Regular:
                $ uv run manage.py runserver
            # With no auto-reload (avoid server auto-update and instability):
                $ uv run manage.py runserver --noreload

        # Or using PIP:
            # Regular:
                $ python manage.py runserver
            # With no auto-reload (avoid server auto-update and instability):
                $ python manage.py runserver --noreload
    

    5) Check the app through the browser:
        http://localhost:8000/
        http://127.0.0.1:8000/