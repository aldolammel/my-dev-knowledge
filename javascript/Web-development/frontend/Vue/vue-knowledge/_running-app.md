VUE: RUNNING THE FRONT-END APP

    PRE) Assuming you already installed a Vue project in your machine:
        .../Vue/1-install-and-first-steps/0-vue-installation-and-setup.txt


    1) On terminal, go to the front-end's folder in your project!
        E.g.
            /my_project/frontend/


    2) (If applicable)
        Check if you are in the right versioning branch:

        # Check if you are versioning this project:
            $ git status

        # If so, be aware if you are in the right branch to use the application:
            /versioning/git/command-checkout.txt


    3) Run the Vue app once you are in the frontend folder:

        3.PRE) Are you using Node locally, right? Probably you need to do it:

            # At first, select the node version configured for this project:
                $ nvm use

                # More about this config:
                    /javascript/NodeJS/2.2-automating-switch-process.txt

        3.1) Running the app:

            >> For Vue projects built by Vite:
                # Using NPM:
                    $ npm run dev
                # Using YARN:
                    $ yarn dev

                >> Check this on browser:
                    http://localhost:5173/

            >> For Vue projects built by Vue-CLI (default):
                # Using NPM:
                    $ npm run serve
                # Using YARN:
                    $ yarn serve
