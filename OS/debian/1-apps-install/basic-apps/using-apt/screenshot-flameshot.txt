

OFFICE TOOL: FLAMESHOT

    Tool that provides smart screenshots.

    >> Install:
        
        >> By terminal (may not the latest version):
            $ sudo apt install -y flameshot
        
        >> Or by .deb file (latest version):
            https://github.com/flameshot-org/flameshot

    

    >> Integration (CRITICAL):

        Problematic versions in Ubuntu using GUI wayland and multi-monitors. Best/fastest version:
        Flameshot v12.1.0. I tried the v13.3.0 and that was absolute chaos!

        1) DON'T set to start with system;

        2) In Ubuntu Shortcuts (Ubuntu settings > Keyboard):

            2.1) Disable the ubuntu original "screenshot" shortcut;

            2.2) Add a "Custom Shortcut" called "Flameshot";

                command: /bin/sh -c 'flameshot gui'
                shortcut: Print

        3) Test it. If okay, restart the system and try again (without opening Flameshot).