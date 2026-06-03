IDE FOR VUE PROJECT: VSCODE

    PRE.1) Assuming you have done this VSCode basic roadmap for the project language(s):

        >> For JavaScript:

            >> with vanilla JS:
                /javascript/ide/vscode/basic-for-javascript.txt

            >> or with TypeScript:
                /javascript/ide/vscode/basic-for-typescript.txt

        >> For Python:
            /python/ide/vscode/basic-for-python.txt


    PRE.2) Assuming the Back-end framework basic project setup is done:

        >> If NO back-end or Vue is the back-end, skip it!

        >> But if Django:
            /python/web-development/django/1-install-and-first-steps/0-django-installation-and-setup.md


    1) VSCode project settings:

        1.1) In the project folder, open this file: .vscode/settings.json;
        1.2) In that file, apply these lines:
            ./examples/settings.json
        1.3) Also, include this file:
            ./examples/extensions.json

        IMPORTANT FOR TEAMS:
            Make sure your .gitignore file is not blocking the .vscode folder and its content in project repository! Once you wouldn't be the only team member in this project, people like to custom their IDEs too.


    2)  Language support (Vue Official by Vue):

        Make VSCode to support the JavaScript framework Vue.

        Download the extension!


    3) Type-Checker:
        .../vue/linter-formatter-typechecker/_type-checker/vue-options.txt


    4) Formatter (Recommended: Prettier):
        /javascript/linter-formatter-typechecker/prettier.txt


    5) Linter:

        >> For projects Single-File-Components (eslint-plugin-vue):
            .../vue/linter-formatter-typechecker/eslint-plugin-vue/installation.md

        >> For NOT SFC projects (<solution_name>):
            /xxxxxxxxxxxxxx


    6) (If applicable)
        For VSCode, re-open the .vscode/settings.json, and set for each Vue and (JS or TS)
        linter/formatter/type-checker the project must use!


---

> > Keep in mind which CSS Framework you wanna use:

    >> Or Bootstrap:
        /web-development/frontend/css/css-libraries-frameworks/bootstrap/

    >> Or Tailwind:
        /web-development/frontend/css/css-libraries-frameworks/tailwind/

    >> Or Bulma:
        /web-development/frontend/css/css-libraries-frameworks/bulma/

> > Keep in mind which CSS Language you wanna use:

    >> Or SCSS/SASS:
        /web-development/frontend/css/scss/

    >> Or Less:
        /web-development/frontend/css/less/
