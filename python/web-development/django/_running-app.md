#### Python > Django:
# Running an app

---
## Before:

1. Keep it in mind: this app is using local db or a cloud one? Case local, is the db service running properly?
2. Assuming you're in the project folder on Terminal;
3. Assuming you got the project's environment activated: [/python/3-virtual-environment/activate-and-deactivate](/python/3-virtual-environment/activate-and-deactivate.md)
4. (If applicable) Assuming you're in the right Git branch: [command-branch](/versioning/git/command-branch.md) and [command-checkout](/versioning/git/command-checkout.md)

---
## 1) Run the app:

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

---
## 2) Check the app through the browser:
http://localhost:8000/ or http://127.0.0.1:8000/
