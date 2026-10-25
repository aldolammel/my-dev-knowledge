#### Python > Django > Models
# Renaming an app (sub-app) safely

---

==Be aware==
So far I couldn't find a way to do that without loose the current database's data!

---

To ~~safely~~ rename a Model Class you must check these things:

1. Rename the model class itself in `/apps/`.
2. Find and replace all `from apps.<oldname>` to `from apps.<newname>`
3. In sub-app's `apps.py`, rename that `class` and the `name` attribute value.
4. In the sub-app's `urls.py`, rename the `app_name`.
5. In sub-app's `consts.py`, if there's any path var using the old name, rename it.
6. (If applicable) In sub-app's `templates/admin/<oldname>/` folder, rename it.
7. In `/core/settings.py`, rename the sub-app listed in `INSTALLED_APPS`.
8. In `/core/urls.py`, rename the sub-app's folder name (`"<oldname>/"`) and its path (`"apps.<oldname>.urls"`).
9. Try a find-and-replace search just to make sure where the old sub-app name is still been used.
   ==Unfortunately:==
10. Delete all migrations-folder content (except the dunder init) from every sub-apps.
11. Execute the database re-creation steps (not just about db): [/python/web-development/django/3-1-models-database/1-recreate-database/\_recreating-db](/python/web-development/django/3-1-models-database/1-recreate-database/_recreating-db.md)

Done.

---
## Moving sub-app folder:
[/python/web-development/django/2-creating-and-deleting-apps/moving](/python/web-development/django/2-creating-and-deleting-apps/moving.md)
## Renaming a model class:
[/python/web-development/django/3-1-models-database/renaming-model-class](/python/web-development/django/3-1-models-database/renaming-model-class.md)


