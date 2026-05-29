#### Python > Project types

# Updating Python in an existing project

    CRITICAL:
        Are you really sure the Python version you need to install is compatible with other techs of the project stack? For example, the back-end framework you are using supports this new Python version? If so, keep going!

    >> Which tool are you using:

        A) Vanilla Python;
        B) UV package manager;

        - - - - -

        A) Vanilla Python - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

            PRE) xxxxxxx

            A.1) xxxxxxxxxxxx

            A.2) xxxxxxxxxxxx


        B) UV - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

            PRE) What is it:
                /python/package-manager/uv/_about-install-and-update.md


            B.1) Check the current Python versions installed and install that you need:

                # In your global local environment, check it:
                    $ uv python list

                # Add the new one, e.g.:
                    $ uv python install 3.13.9


            B.2) In your project folder/environment, set up:

                # Defining to UV which Python version the project must run, e.g.:
                    /python/package-manager/uv/pin-python-version.md

                # (If applicable) In pyproject.toms file, update Python version:
                    [project]
                    ...
                    requires-python = "==3.13.9"  # Or ">=3.13.7,<3.14"

                # (If applicable) In pyproject.toml file, if using RUFF:
                    [tool.ruff]
                    ...
                    target-version = "py313"  # Python (py313 means newest of 3.13 = 3.13.9) <------

                # (If applicable) In pyproject.toml file, if using MyPy:
                    [tool.mypy]
                    ...
                    python_version = "3.13"  # 3.13 means newest of 3.13 = 3.13.9  <----------------

                # Sync the environment (UV will recreate venv with new Python):
                    /python/package-manager/uv/auto-installation-with-sync.md

                # Deactive and active the project environment:
                    /python/3-virtual-environment/activate-and-deactivate.txt

                # Verify the Python version in the environment
                    $ uv run python --version


            B.3) (Optional)
                Uninstall unwanted Python versions:
                    /python/package-manager/uv/uninstall-python-old-version.md

---
