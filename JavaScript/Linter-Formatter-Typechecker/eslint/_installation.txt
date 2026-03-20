

ESLINT: INSTALL AND INTEGRATION


    1) INSTALLATION - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        1.1) Installing ESLint core and its configuration package only as DEV dependencies:

            # Using NPM:
                $ npm install -D eslint @eslint/js               <-- -D means it's a DEV dependency!
            
            # Or using xxx:
                $ xxxxxxx

            # Check if everything's right on the front-end folder's package.json file!
        

        1.2) Install 'globals' that's an ESLint configuration package to provide global vars for different environments (browser, node, etc) to ESLint:

            $ npm install -D globals
        

        1.3) Install the ESLint extension (by Microsoft) in your IDE;


    
    2) INTEGRATION - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        2.1) Check in front-end folder root if you have the eslint.config.js file. If not, create it:
            ./eslint.config.js

        2.2) Basic IDE integration for ESLint:
            >> For VSCode:
                ./vscode-eslint-as-formatter.json

        2.3) (If applicable)
            Case you are using Vite as your JS Build-tool, make Vite recognize the ESLint work:

                ./vite-plugin-eslint.txt
        
        2.4) (If applicable)
            In case the project's demanding Prettier (formatter), make the ESLint doesn't conflict with that:

                2.4.PRE) Assuming your frontend folder already has the Prettier config file:
                    .../Linter-Formatter-Typechecker/prettier/.prettierrc
                
                2.4.1) Install Prettier and the critical integration packages:
                        
                    $ npm install -D eslint-config-prettier eslint-plugin-prettier

                    # Check if everything's right on the front-end folder's package.json file!

                2.4.2) Tweak the ESLint config file:
                    
                    KEEP IN MIND:
                        Once you are here it's because you wanna use Prettier. That said, set all ESlint FORMATTING stuff to Prettier, meanwhile ESLint focuses only
                        in linting!

                    >> Adapt this file below in your frontend project to consider Prettier with ESLinter partner:
                        ./eslint.config.js-for-prettier

                    >> Replace the current IDE configuration:
                        >> For VSCode:
                            ./vscode-prettier-as-eslint-formatter.json


        2.5) (Optional) 
            Add the ESLint as a script in package.json file in the frontend folder to make ESLint terminal commands available:
                ./package.json

        2.6) (If applicable) 
            In case of Git versioning, add it in your .gitignore file:
            
                ### Node.js ###
                ...
                # Optional eslint cache
                .eslintcache

        2.7) (If applicable / Optional)
            In case your project is in Python, open the pyproject.toml file and include this
            in there:

                # ESLint linter settings:
                # All settings of that is in /frontend/eslint.config.js

