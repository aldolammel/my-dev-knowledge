#### OS > Linux > Debian

# Installing apps

    PRE.1) Prepare the system:
        ./0-preparing-the-system.md

    PRE.2) Install the basic apps:
        ./basic-apps/

            >> @aldolammel Ubuntu's default browser = Firefox (non-snap)
                ./basic-apps/using-apt/browser-firefox.md


    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


    INSTALL AND UNINSTALL APPS:


        IMPORTANT:
            When you run "sudo apt install <package>", APT searches through its package index — a db of all available packages from repositories you've already added to your system. This index is created and updated when you run "sudo apt update".


        >> Installing:

            >> From a repository (MOST USED):
                $ sudo apt install -y <package_name>                 <-- '-y' skip install question.

                >> Finding a package name installed:
                    ./finding-installed-apps.md

                >> Check apt-update repo list:
                    ./checking-app-is-in-repo-list.md

            >> From a local file:
                # Go to the installation file current folder and:
                    $ sudo apt install ./<filename>.<file_extension>
                        E.g.
                            $ sudo apt install ./obsidian.deb


        >> Removing:

            >> .deb:
                $ sudo apt remove <package_name>

                    # Clean up APT cache:
                        $ sudo apt autoclean

                    # Remove unused old apps/dependencies:
                        $ sudo apt autoremove

            >> Snap:
                $ sudo snap remove <app_name> || true

---
