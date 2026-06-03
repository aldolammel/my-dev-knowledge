PRETTIER: VUE INTEGRATION

    WHAT IS PRETTIER:
        ./_about.md


    >> Using VSCode as IDE:

        PRE) Assuming you already installed Prettier in your IDE/project:
            /javascript/linter-formatter-typechecker/prettier/installation.md

        1)  (NOT RECOMMENDED USE PRETTIER AS VUE FORMATTER)
            If you wanna a better formatter for Vue, use the ESLint for VUE, otherwise, use prettier:

            Edit your VSCode profile that you are using Vue and:

            // VUE SETTINGS
            "[vue]": {
                "editor.defaultFormatter": "esbenp.prettier-vscode",
                "editor.tabSize": 2,
                "editor.indentSize": "tabSize",
                "editor.insertSpaces": true,
            },

---

BETTER VUE FORMATTER:
.../linter-formatter-typechecker/eslint-plugin-vue/
