

DJANGO: ITS FILES AND FOLDER STRUCTURE


    >> How will the front-end be built?

        A) Django as entire solution for back and front-end;
        B) Or Django as back-end only (for external frontend solution);

    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


        A) Django as ENTIRE solution for back and front-end:

            my_project_name/
            ├── .venv/                       # Virtual env folder where Django things are installed.
            │
            ├── core/                        # Django core folder.
            │   ├── __init__.py
            │   ├── consts.py                # Where is defined global Django constant variables.
            │   ├── context_processors.py    # Data/context to make available to the entire project.
            │   ├── settings.py              # Main configuration file of the entire project.
            │   ├── urls.py                  # Main URL configuration for the entire project.
            │   └── wsgi.py                  # xxxxxxxx.
            │
            ├── apps/
            │   ├── app1/               # Example of a 'sub-app' of the main-app (project folder).
            │   │   ├── migrations/     # Folder where all db logic/structure changes are tracked.
            │   │   │   └── ...
            │   │   │
            │   │   ├── services/       # When a utils is not generic, demanding db, managing files.
            │   │   │   └── ...         # Every service/method should be a specific file.
            │   │   │
            │   │   ├── templates/      # Where custom CMS html for this sub-app is located.
            │   │   │   └── admin/      # Local CMS interface customizations.
            │   │   │       └── ...
            │   │   │
            │   │   ├── __init__.py     # Django sub-app init file (empty).
            │   │   ├── admin.py        # All CMS needs of this specific app are defined here.
            │   │   ├── apps.py         # Where this app's name is defined for the entire system.
            │   │   ├── consts.py       # Local constant vars library.
            │   │   ├── forms.py        # Form classes tied w/ Models or receiving data from Views.
            │   │   ├── lang.py         # Language library, important for multilanguage systems.
            │   │   ├── models.py       # All database schema for this specific app is defined here.
            │   │   ├── serializers.py  # Where this app builds its APIs.
            │   │   ├── signals.py      # xxxxxxxx.
            │   │   ├── tests.py        # xxxxxxxx.
            │   │   ├── urls.py         # URL configuration specific for this app.
            │   │   ├── utils.py        # Only funcs, with no db-access, stateless, agnostic.
            │   │   ├── utils_models.py # <--- MAYBE NOT NEEDED!
            │   │   ├── validators.py   # Custom validators to validate things through the sub-app.
            │   │   └── views.py        # Data/context from this app to send to the template.
            │   │
            │   ├── app.../
            │   │   └── ...
            │   │
            │   └── __init__.py        # Makes Apps folder to be a package of apps.
            │
            ├── media/                 # xxxxx
            │
            ├── static/                # xxxxx
            │   ├── js/                # xxxxx
            │   ├── css/               # xxxxx
            │   └── dist/              # xxxxx
            │
            ├── templates/               # Django templates.
            │   ├── admin/               # Global CMS interface customizations.
            │   │    └── base_site.html    
            │   │
            │   ├── components/            # If using Django front-end, reusable template fragments.
            │   │   └── ...
            │   │
            │   └── pages/                 # If using Django front-end, html of pages.
            │       ├── home.html      
            │       ├── about.html
            │       └── ...
            │
            ├── .env                   # Exclusive back-end environment variables.
            ├── .gitignore             # For Git repository untrack specific files and folders.
            ├── manage.py              # Command-line utility for Django core.
            └── pyproject.toml         # List of all Django project's (backend) dependencies.


    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


        B) Django as back-end only (for external frontend solution):

            my_project_name/
            ├── .venv/                 
            │
            ├── core/                  
            │   ├── __init__.py        
            │   ├── consts.py       
            │   ├── settings.py        
            │   ├── urls.py            
            │   └── wsgi.py            
            │
            ├── frontend/         # Where the front-end solution will be installed.
            │
            ├── apps/
            │   ├── app1/              
            │   │   ├── migrations/    
            │   │   ├── __init__.py    
            │   │   ├── admin.py       
            │   │   ├── apps.py        
            │   │   ├── forms.py
            │   │   ├── models.py      
            │   │   ├── serializers.py  
            │   │   ├── tests.py       
            │   │   ├── urls.py 
            │   │   └── views.py       
            │   │
            │   ├── app.../
            │   │
            │   └── __init__.py  
            │
            ├── media/ 
            │
            ├── static/                # keep it empty once Django needs for collectstatic's command.
            │
            ├── templates/              
            │   └── admin/  
            │       └── base_site.html     
            │
            ├── .env
            ├── .gitignore
            ├── manage.py
            └── pyproject.toml         # List of all Django project's (backend) dependencies.