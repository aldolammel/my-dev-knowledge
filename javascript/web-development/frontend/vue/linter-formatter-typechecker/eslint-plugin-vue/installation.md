VUE > TEMPLATE LINTER > ESLINT: INSTALLATION

    PRE.1) Assuming you have done first steps to create a Vue project:
        .../vue/1-install-and-first-steps/1-install-new-project.md

    PRE.2) Assuming you already are in the frontend folder of the project on terminal;

    PRE.3) Assuming you already installed the ESLint for JavaScript/TypeScript:
        /javascript/linter-formatter-typechecker/eslint.txt

    PRE.4) Your Vue project is a SPA one!
        ./_about.md


    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


    1) Install the ESLint plugin for Vue (eslint-plugin-vue) as development dependency:

        https://eslint.vuejs.org/

        # Using NPM:
            $ npm install -D eslint-plugin-vue                          <-- -D means DEV dependency!

        # Or using XXX:
            xxxxxxxx

        # Check if everything's right on the front-end folder's package.json file!

    2) Edit the ESLint config file on the Vue project root ('frontend', e.g.):
        ./eslint.config.js

    3) In vite.config.js file:
        //...
        import eslintPlugin from 'vite-plugin-eslint'
        //...
            plugins: [
                vue(),
                //...
                eslintPlugin({
                    include: ['src/**/*.js', 'src/**/*.vue', 'src/*.js', 'src/*.vue'],
                    exclude: ['node_modules/**', 'dist/**'],
                    cache: false
                })
            ],

    4) Basic IDE configs for Vue:

        >> For VSCode:

            1) In /project/.vscode/settings.json file:

                // VUE SETTINGS
                "[vue]": {
                    "editor.defaultFormatter": "dbaeumer.vscode-eslint", // ESLint
                    ...
                },
