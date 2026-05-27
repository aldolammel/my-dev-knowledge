

INTERNET TOOL: MOZILLA FIREFOX

    Since Ubuntu 22.04, Canonical decided to ship Firefox only as a Snap in the main repository. The .deb version is maintained separately by the Mozilla Team PPA.


    1) Ubuntu already comes with Firefox but not the real one. It comes with the SNAP version. So, at first, delete that version:
        
        $ sudo apt remove firefox
    

    2) Force Ubuntu just consider the .deb version:

        $ sudo nano /etc/apt/preferences.d/mozilla-firefox

            Package: firefox*
            Pin: release o=LP-PPA-mozillateam
            Pin-Priority: 1001


    3) Update the system;

        >> (NOT NEEDED IF ALREADY ONBOARD OF THE OS) Adding .deb version as repository:
            $ sudo add-apt-repository ppa:mozillateam/ppa


    4) Install it:
        $ sudo apt install -y firefox




- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


XXXXXXXXXXXXXXXXX:
    /xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx