"""
VIRTUAL ENVIRONMENT:

A virtual environment is a way to have multiple, parallel instances of the Python interpreter, each with different sets
of packages and different configurations. Each virtual environment contains a discrete copy of the Python interpreter,
including copies of its support utilities. The packages installed in each virtual environment are seen only in that
virtual environment and no other. Even large, complex packages with platform-dependent binaries can be corralled off
from each other in virtual environments.


1) CREATING A VIRTUAL ENVIRONMENT:

1.1) GO to the terminal;
1.2) Go to the folder that you want to install the virtual environment;
1.3) In the folder, type through Terminal to create the virtual environment: virtualenv venv_unique_name
    If the command wasn't recognized, install the virtualenv module: pip install virtualenv


2) CONFIGURING:

2.1) In lower-right-corner of pycharm, select 'Add new interpreter' > 'Local interpreter'.
2.2) Select 'Existing' and, after that, select '<venv_of_your_project>/Scripts/python.exe'
2.3) Open the Python Interpreter windows (Ctrl+alt+0+S)
2.4) In 'Python interpreter' drop-menu, select 'Show all'.
2.5) Find the new environment and unselect the "Associate this venv with the current project".
2.6) Finally, rename the environment to make its selection easier.

"""