

FEDORA: CHECK THE CURRENT DNF-UPDATE REPO LIST


    >> Checking all repos (using old "xxxxxxxxxx" formats and new "URIs" ones):
        
        <See the equivalent for fedora>
    
    
    >> Only for a specific app:

        <See the equivalent for fedora>

    
    >> If it's there, check if the apt-update is considering that:
        $ sudo dnf update | grep -i <app-name>


    >> More details about a repos (which priority, etc):
        <See the equivalent for fedora>

        $ apt-cache policy
        # Or:
        $ apt-cache policy <app_name>

        IMPORTANT:<See the equivalent for fedora>
            500 = It's just a how high that version of the app will be considered by apt-update when you upgrade the system.



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


>> REMOVING REPO:
    /xxxxxxxxxxxxxxxxxxx