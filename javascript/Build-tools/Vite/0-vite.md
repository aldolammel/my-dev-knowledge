

JAVASCRIPT BUILD-TOOL: VITE


    Vite (pronounced "veet", and from the same creator of Vue.JS) is a JS build tool and a front-end development server running over Node.JS (engine), and it's used in JS and TypeScript projects.
    
    https://vite.dev/
    
    It's used primarily to solve the performance and experience problems that come with traditional build tools like Webpack when projects grow large. 
    
    And Vite is framework-agnostic so through its plugins, Vite can support Vue, React, Svelte, Solid, for example.

    

    1) (Optional)
        Figure out if Vite is installed and/or update Vite:

        1.1) On terminal, go to the front-end project folder. If you are using Vite globally (not recommended), do it anywhere:
    
            # Shows the installed Vite version and its dependencies:
                $ npm list vite

            # Updating to the latest version:
                $ npm update vite
            # Or updating to a specific version:
                $ npm install vite@6.3.5

            # Checking again the current Vite version:
                $ npm list vite


    2) Install Vite:

        2.1) Which method do you wanna use:
        
            2.1A) Install Vite for the first time in a new front-end project (scaffolding tool);
            2.1B) Re-install Vite in an existing front-end project;
            
            - - - - 
            
            2.1A) Install Vite for the first time in a new front-end project - - - - - - - - - - - -
                
                2.1A.1) On terminal, go to project's backend folder (NOT the front-end folder)!

                2.1A.2) Install Vite locally (without -g) and start the project creation:

                    $ npm create vite@latest
                    
                    # This process will create the Vue project folder, asking you the folder's name soon! Recommended Vite settings, just follow the prompt instructions/options:

                        - Project name: = by convention, use 'frontend' or just a '.' if
                                        you already are in the root of the 'frontend' folder.
                        
                        - Framework = vue

                        - Variant = JavaScript

                        - Router? In case of SPA project, yes, but later!   (and MPA projects ??????????????)
                            Vite has NO standard solution, but Vue does (Vue-Router)!
                        
                        - CSS Pre-processors? Yes but later!
                            Vite 6+ has native support for: .scss, .sass, .less, .styl, 
                            .stylus!
                        
                        - Babel? No:
                            Vite already convert JS code for all browsers;
                        
                        - Linter/Formatter? Yes but later!
                            Vite has NO standard solution;
                
                
            2.1B) Re-install Vite in an existing front-end project - - - - - - - - - - - - - - - - -
            
                TIP:
                    Do you need uninstall Vite first?
                        ./uninstall.txt
                
                2.1B.1) Go to the front-end project folder:
                    E.g.
                        /my_project/frontend/
                    
                2.1B.2) Re-install Vite:
                    >> Using NPM:
                        # Install a specific major version (recommended for stability)
                            $ npm install vite@^7    <--    means the latest version of v7.
                                                            If you run vite@latest, probably you'll face compatible errors with Tailwind or other frameworks that depends of Vite plugins and are not ready for Vite latest version.

                        # Install the absolute latest version (may cause compatibility issues)
                            $ npm install vite@latest

                    >> Using YARN:
                        $ yarn add vite@^7
        
        
            - - - - 
            

        2.2) Plugins for your linter:
            
            # Case you're using:
            
                >>  ESLint:
                    /vault/javascript/Linter-Formatter-Typechecker/eslint/vite-plugin-eslint.txt


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

