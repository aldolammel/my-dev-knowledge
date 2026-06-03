

NODE.JS: HOW TO UNINSTALL


    >> What do you want to uninstall:

        A) Just a NPM component;
        B) The entire Node;

        - - - - - - 

        A) Just a NPM component - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

            # Locally:
                
                # In the project folder, check the current packages are installed on this project:
                    $ npm list
                
                # So, again, in the project folder, uninstall the desired package/component:
                    $ npm uninstall <package_name>
                        e.g.
                            $ npm uninstall naive-ui         <-- without '@' and version numbers

            # Globally:

                # In your user root folder, check the current packages are installed on this machine:
                    $ npm list
                
                # No matter where you are, uninstall the desired package/component globally (-g):
                    $ npm uninstall -g <package_name>
                        e.g.
                            $ npm uninstall -g naive-ui       <-- without '@' and version numbers


        B) The entire Node - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

            BE AWARE:
                Maybe you don't need to uninstall. With NVM (Node Version Manager) installed, you can switch the installed version easily:
            
                    ./2.1-switch-versions.txt

                BK) Uninstall Node previously installed globally;
                BL) Uninstall only a specific Node version previously installed;

                - - - - 

                BK) Uninstall Node previously installed globally - - - - - - - - - - - - - - - - - -

                    BK.1) Check the nodejs version (not 'node' for this case):
                        $ nodejs -v
                        
                            # Double-check if the nodejs has a global folder:
                                $ which nodejs   <-- if something returned, it's installed globally!

                    BK.2) Uninstall nodejs and its package manager (if applicable):
                        $ sudo apt remove nodejs npm
                            
                            # Removing configuration files (optional):
                                $ sudo apt purge nodejs npm
                        
                        # Removing the uninstalled files:
                            $ sudo apt autoremove

                        # Check if nodejs still exist globally:
                            $ nodejs -v
                            $ which nodejs

                            # (Optional) If nodejs persists globally:
                                # Remove global npm packages directory (if it exists)
                                    $ sudo rm -rf /usr/local/lib/node_modules
                                # Remove npm cache
                                    $ sudo rm -rf ~/.npm
                                # Remove any remaining Node.js related files
                                    $ sudo rm -rf /etc/apt/sources.list.d/nodesource.list*
                                # Close the current Terminal, and check everything once again!
                                
                
                BL) Uninstall only a specific Node version - - - - - - - - - - - - - - - - - - - - -

                    
                    >> Which Node Version Manager are you using:

                        BLZ) NVM;
                        BLX) Docker;

                        - - - - - -

                        BLZ) NVM - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

                            CRITICAL:
                                If you're using automation methods to switch the Node versions, be aware about what method you're using for other current projects:

                                    ./2.2-automating-switch-process.txt

                            BLZ.1) That said, check which versions you got installed:
                                $ nvm list node

                            BLZ.2) Uninstall a specific Node version:
                                $ nvm uninstall <version>            <-- can be 23 or exact 23.11.0.


                        BLX) Docker - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                            Soon!
                    

