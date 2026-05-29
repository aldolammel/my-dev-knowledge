

DJANGO RE-INSTALLATION: USING PIP AS PACKAGE MANAGER (PYTHON BUILT-IN SOLUTION)

    
    PRE.1) If you wanna install a new brand project, skip this roadmap, and go to:
        ./2-install-project-with-pip.md
    

    PRE.2) Make sure you already updated PIP:
        /vault/python/package-manager/pip/_about.md


    PRE.3) IDE steps:

        >> Select through the IDE GUI which User Profile this project demands!
                # Aldo's profile backups:
                    /vault/ide/vscode/user-profiles-bkp/
                    /vault/ide/pycharm/xxxxxxxxxxxxxxxx/

        >> Open this new folder in your IDE;


    PRE.4) Active the project environment:
        /vault/python/3-virtual-environment/activate-and-deactivate.txt


    1) Uninstall the current Django version:
        $ pip uninstall Django


    2) Install the new Django version:
        $ pip install Django==5.0

        # Check the current installed version:
            $ python -m django --version


    3) About the integration update, update the Django version in these files:
        
        /project_folder/pyproject.toml
            # More about:
                xxxxxxxxxxxxxxxxxxxxxxxx

        # Or:
        
        /project_folder/requirements.txt
            # More about:
                /vault/python/package-manager/pip/auto-installation-from-requirements-file.md
            

        


    ---- NEED TO REVIEW: ----------------------------


    X) migration or makemigrations is needed again?


    3) (Optional)
        If you have multilingual support in your project:

        >> With Gettext module installed:
            
            $ uv run manage.py makemessages --all
            $ uv run manage.py compilemessages

        

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


MAKE SURE YOU FINISHED ALL THESE STEPS:
    ./0-django-installation-and-setup.md