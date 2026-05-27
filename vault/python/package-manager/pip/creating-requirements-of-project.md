#### Python > Package Manager > PIP
# Creating the requirements.txt of a project


==Attention!==
This method (of install requirements via requirements.txt) is old nowadays, fragile, fakely "automatic" and error-prone, where there is no differencies between what is mandatory, what is just for development, once it ignores the pyproject.toml file.

Use the UV method that is based on pyproject.toml file instructions:
/vault/python/package-manager/uv/creating-requirements-of-project.md

That said, let's go:

The 'requirements.txt' file is a legacy way (old) to install the entire project's dependencies in a row. This file ignores completely the pyproject.toml if the requirements file was generated automatically by 'pip freeze'. This method also ignores other packages that didn't was installed through pip command. 

        

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


    >> How to create it:

        1) In your app folder, with the virtual environment activated, do it:

            Win:
                $ 

            Linux/Ubuntu:
                $ python3 -m pip freeze > requirements.txt

            Mac:
                $


    >> How to use it:

        1) Move the requirements.txt file to the project root;

        2) Once you already got the right virtual environment activated, upgrade the pip:

            /vault/python/package-manager/pip.txt

        3) Install the packages at once:

            $ python3 -m pip install -r requirements.txt

        4) Check if everything is fine:

            $ python3 -m pip list