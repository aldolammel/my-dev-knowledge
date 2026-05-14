

VITE: UNINSTALLING

    PRE) Assuming you already are in the front-end project folder!

    1) Do it:
    
        # Option 1: Direct installation (overwrites current version)
            Just execute the re-install without any uninstalling:
                ./0-vite.txt

        # Option 2: cleaner approach uninstalling this first
            $ npm uninstall vite
            $ npm install vite@^7

        # Option 3: If you have dependency issues
            $ rm -rf node_modules package-lock.json
            $ npm install
            $ npm install vite@latest