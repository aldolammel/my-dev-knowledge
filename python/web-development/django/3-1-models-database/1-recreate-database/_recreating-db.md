#### Python > Django:
# Re-creating the project database

---
## If the db structure is good, and you just wanna erase its stored data:

If it's okay to preserve tables and columns of the current database, just do a `flush` on it: [/python/web-development/django/3-1-models-database/1-recreate-database/clean-database](/python/web-development/django/3-1-models-database/1-recreate-database/clean-database.md)

---
## If you need to re-create your db from the beginning:

==Attention for multilingual projects:==
If your app is multilingual and are using prefix_language mandatory, your new db must be created and, right after, you must include on language table at least one language for you be able to use the CMS! So be aware of this!
        
**1) Delete the current database:**

- [ ] Pick your case for deletion:
- PostgreSQL: [/database/PostgreSQL/deleting-db](/database/PostgreSQL/deleting-db.md)
- MySQL: soon...
- MariaDB: soon...
- SQLite: soon...

**2) Create the new database:**

- [ ] Pick your case for creation:
- PostgreSQL: [/database/PostgreSQL/creating-db-locally](/database/PostgreSQL/creating-db-locally.md)
- MySQL: soon...
- MariaDB: soon...
- SQLite: soon...

**3) (If applicable) Make sure you are in the right versioning branch:**

- [ ] Check it: [/versioning/git/command-checkout](/versioning/git/command-checkout.md)
            
**4) Delete all migration-folder content (except the dunder init):**

- [ ] Check if you are visualizing the `__pycache__` folder. It should be deleted too, but the project settings could be hidden them!

**5) And keep going:**

1. [ ] Edit your `.env` file as needed (the new db name, for example);
2. [ ] BE AWARE: close all Terminals/Prompts you ran with the old `.env` before (it avoids issues with old environment variables)
3. [ ] Run `makemigrations` for each sub-app, and then run `migrate` for them;
4. [ ] (If applicable) If you'll use the CMS, run `createsuperuser` command;
5. [ ] (If applicable) For multilingual apps, and have `prefix_language` mandatory, add manually at least one language in the language table for you are allowed to use the CMS;
6. [ ] Run `runserver` to test Django!

---
## How to re-install only Django:
[/python/web-development/django/1-install-and-first-steps/1-reinstall-new-copy](/python/web-development/django/1-install-and-first-steps/1-reinstall-new-copy.md)

