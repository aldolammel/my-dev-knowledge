FLASK: INSTALLING AND SETUP

    1) Which scenario is your case:

        1A) This machine and IDE are ready for Flask projects, and I got a brand new project:

            >> Skip this file, jumping to this one:
                ./1-install-new-project.md


        1B) This machine and IDE are ready for Flask projects, and I'm just re-installing Flask for an existing app (or re-installing the entire project):

            >> Skip this file, jumping to this one:
                ./1-reinstall-new-copy.md


        1C) This machine (or IDE) is new (for example, after the OS installation) and I need to prepare it to run Flask projects:

            >> Keep yourself in this roadmap file!


        - - - - -


        1C) This machine (or IDE) is new! Preparing it to everything about Flask - - - - - - - - -

            1C.PRE.1) Python interpreter (if needed);
                /python/1-python-installation/

            1C.PRE.2) Create the project folder, and get it:
                $ mkdir <project_folder>
                $ cd <project_folder>

            1C.PRE.3) DON'T create the .venv yet (so is NOT need to activate environ for now)!

            1C.PRE.4) IDE, select through the IDE GUI which User Profile this project demands!
                        # Aldo's profile backups:
                            /ide/vscode/user-profiles-bkp/
                            /ide/pycharm/xxxxxxxxxxxxxxxx/

            1C.PRE.5) IDE, language setup:
                >> VSCode:  /python/IDE-softwares/vscode/basic-for-python.txt
                >> PyCharm: /python/IDE-softwares/pycharm/basic-for-python.txt

            1C.1) IDE, framework setup:
                >> VSCode:  .../flask/IDE-softwares/vscode/basic-for-flask.txt
                >> PyCharm: .../flask/IDE-softwares/pycharm/basic-for-flask.txt

            1C.2) Install Flask for a specific project:

                >> Using UV (recommended, smarter):
                    ./2-install-project-with-uv.md

                >> Or using PIP:
                    ./2-install-project-with-pip.md


        - - - - -


    2) Once Flask project already installed, let's ask us again about the current case:

        A) This machine and IDE are already for Flask projects, and I got a brand new project:

            >> Skip this file, jumping to this one:
                ./1-install-new-project.md

        B) This machine and IDE are ready for Flask projects, and I'm just re-installing Flask for an existing app (or re-installing the entire project):

            >> Skip this file, jumping to this one:
                ./1-reinstall-new-copy.md

---

    MAKE SURE YOU ALREADY FINISHED ONE OF THESE ROADMAPS:

        >> FLASK as back and front-end:
            .../flask/0-new-project/web-project-flask-only.md

        >> FLASK with VUE as front-end:
            .../flask/0-new-project/web-project-flask-with-vue.md

        >> FLASK with REACT as front-end:
            .../flask/0-new-project/web-project-flask-with-react.md

        >> FLASK with ANGULAR as front-end:
            .../flask/0-new-project/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
