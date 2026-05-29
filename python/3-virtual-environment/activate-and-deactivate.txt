

ACTIVATING OR DEACTIVATING A VIRTUAL ENVIRONMENT:


    >> Activating:

        UBUNTU:
            $ . <venv_name>/bin/activate


        WINDOWS:
            $ <venv_name>\Scripts\activate

            # Execute this command below if you're not allow to activate an env via Terminal:
            # In PowerShell as administrator:
            
                $ Set-ExecutionPolicy Unrestricted -Scope LocalMachine
                # or:
                $ Set-ExecutionPolicy Unrestricted -Scope CurrentUser
        
        
        MAC:
            $ source <venv_name>/bin/activate

        Important: the feedback that you're using the right environment is the environment name
                    is flagged in parentheses before the prompt command line as "(venv_name) ..."



    >> Deactivating:

        $ deactivate



    FOR PYCHARM:
    Reconfigure as needed:
        1) In lower-right-corner of pycharm, select 'Add new interpreter' > 'Local interpreter'.
        2) Select 'Existing' and, after that, select '<venv_of_your_project>/Scripts/python.exe'
        3) Open the Python Interpreter windows (Ctrl+alt+0+S)
        4) In 'Python interpreter' drop-menu, select 'Show all'.
        5) Find the new environ and unselect the "Associate this venv with the current project".
        6) Finally, rename the environment to make its selection easier.


    FOR VSCODE:
    Selecting the Interpreter:
        1) Ctrl+Shift+P
        2) Type "Python Interpreter"
        3) Select the environment desired.