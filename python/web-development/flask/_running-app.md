#### Python > Flask
# Running an app

---
## Before:

1. Keep it in mind: this app is using local db or a cloud one? Case local, is the db service running properly?
2. Assuming you're in the project folder on Terminal.
3. Assuming you got the project's environment activated: [/python/3-virtual-environment/activate-and-deactivate](/python/3-virtual-environment/activate-and-deactivate.md)
4. (If applicable) Assuming you're in the right Git branch (commands [branch](/versioning/git/command-branch.md) and [checkout](/versioning/git/command-checkout.md)).

---
## Run the app:

Using UV:
```bash
# Running with no cache:
$ uv run flask run --debug
# Regular:
$ uv run flask run
```
Or using PIP:
```bash
# Running with no cache:
$ python flask run --debug
# Regular:
$ python flask run
```

Check the app through the browser:
http://localhost:5000/
http://127.0.0.1:5000/
