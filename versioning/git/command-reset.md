#### Versioning > Git > Command
# Reset

---

Moves the current branch pointer to a specific commit, optionally modifying the staging area and working directory.

---
## 1) Reset a branch to match remote exactly:

Select the right local branch:
```
git checkout <branch_name>
```
Reset it based on its remote copy: 
```
git reset --hard origin/<branch_name>
```

---
## 2) (If applicable) Consider to update your development environment:

For Python/**Django**: 
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---
