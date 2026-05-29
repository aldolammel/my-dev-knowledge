#### Python > Django > Project types

# Updating Django in an existing project

    >> Considering a Python update too:
        /python/0-new-project/3-update-python-version-in-a-project.md

    >> Which tool are you using:

        A) Vanilla Python;
        B) UV package manager;

        - - - - -

        A) Vanilla Python - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

            PRE-A.1) In case you've just updated Python in the project:

                I. xxxxxxxxxxx
                II. xxxxxxxxxxxxxx
                III. xxxxxxxxxxxxxxxxxxx
                IV. Update Python version in the project config files:

                    >> If using requirements.txt:
                            xxxxxxxxxxxxxxxxx

                    >> If using pyproject.toml:

                        # In pyproject.toml file, do it like this example:
                            requires-python = ">=3.13.3"
                            # Or if you want to allow 3.13.3 and above but below 3.14:
                            # requires-python = ">=3.13.3, <3.14"

            A.1) xxxxxxxxxxxxxxxxxxxx

            A.x) xxxxxxxxxxxxxxxxxxxx

            A.x) xxxxxxxxxxxxxxxxxxxx


        B) UV - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

            PRE-B.1) What is it:
                /python/package-manager/uv/_about-install-and-update.md

            PRE-B.2) In case you've just updated Python in the project:

                I. Test Django:
                    $ uv run manage.py check

                II. Run migrations check:
                    $ uv run manage.py makemigrations --check --dry-run

                III. Test the dev server:
                    $ uv run manage.py runserver

                IV. Update Python version in the project config files:

                    >> If using requirements.txt:
                        xxxxxxxxxxxxxxxxx

                    >> If using pyproject.toml:

                        # In pyproject.toml file, do it like this example:
                            requires-python = ">=3.13.3"
                            # Or if you want to allow 3.13.3 and above but below 3.14:
                            # requires-python = ">=3.13.3, <3.14"

                        # Now, let's update the uv.lock and .python-version dynamically, running again the UV sync:
                            /python/package-manager/uv/auto-installation-with-sync.md

                        # Check those files to confirm changes!


            B.1) Make a project's db backup!
                /database/PostgreSQL/backup.txt
                /database/MySQL/mysql-backup.txt
                /database/MariaDB/mariadb-backup.txt
                /database/SQLite/sqlite-backup.txt

            B.2) Update the Django, going to the project folder and, e.g.:
                $ uv add "django>=5.2.7,<5.3"
                    # Check the pyproject.toml file if the new version was correctly declared!

            B.3) Update all dependencies to ensure compatibility with new Django version:
                /python/package-manager/uv/upgrade-dependencies.txt

            B.4) Test Django:

                # Core Django check:
                    $ uv run manage.py check
                # Make sure migrations won't conflict:
                    $ uv run manage.py makemigrations --check --dry-run
                # (If needed) Execute the migration:
                    $ uv run manage.py migrate
                # Run Django:
                    $ uv run manage.py runserver

---

    >> XXXXXXXXXXXX
