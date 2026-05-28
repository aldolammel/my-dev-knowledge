#### OS > Linux > Debian

# Updating the system

    $ sudo apt update       ← update the repositories list
    $ sudo apt upgrade      ← install the available updates
    $ sudo apt autoremove   ← removes all dependencies installed but not needed anymore.
    $ sudo apt autoclean    ← cleans the local package cache by removing downloaded obsolete files.

    # Or

    $ sudo apt full-upgrade -y
