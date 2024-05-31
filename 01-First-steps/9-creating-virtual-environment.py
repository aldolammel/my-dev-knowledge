"""
VIRTUAL ENVIRONMENT:

A virtual environment is a way to have multiple, parallel instances of the Python interpreter, each with different sets
of packages and different configurations. Each virtual environment contains a discrete copy of the Python interpreter,
including copies of its support utilities. The packages installed in each virtual environment are seen only in that
virtual environment and no other. Even large, complex packages with platform-dependent binaries can be corralled off
from each other in virtual environments.


1) CREATING:
    1.1) GO to the terminal;
    1.2) Go to the folder that you want to install the virtual environment;
    1.3) In the folder, type through Terminal to create the virtual environment: virtualenv venv_unique_name
        If the command wasn't recognized, install the virtualenv module: pip install virtualenv


2) ACTIVATING
    2.1) Go to the terminal;
    ON WINDOWS:  2.2) Type: <venv_name>/Scripts/activate
    ON LINUX:    2.2) Type: source <venv_name>/bin/activate

        Important: the feedback that you're using the right environment is the environment name is flagged in
        parentheses before the prompt command line as "(venv_name) ..."


3) RECONFIGURE AS NEEDED:
    3.1) In lower-right-corner of pycharm, select 'Add new interpreter' > 'Local interpreter'.
    3.2) Select 'Existing' and, after that, select '<venv_of_your_project>/Scripts/python.exe'
    3.3) Open the Python Interpreter windows (Ctrl+alt+0+S)
    3.4) In 'Python interpreter' drop-menu, select 'Show all'.
    3.5) Find the new environment and unselect the "Associate this venv with the current project".
    3.6) Finally, rename the environment to make its selection easier.

"""