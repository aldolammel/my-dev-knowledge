

SCSS VARIABLES: VARIABLES ACROSS COMPONENTS

    >> Create this file in your project:

        // /project-folder/src/assets/styles/vars.scss
            
            $body_color: #000000;
            $primary-color: #1867c0;
            $text-color: #2c3e50;
            $spacing-unit: 8px;
            $font-family: sans-serif;

    >> Call the variables in the main SCSS file:

        // /project-folder/src/assets/styles/app.scss
            
            // (first code lines):
            @use "sass:color";
            // (first code lines) Theme variables:
            @use "@/assets/styles/vars";
            // External fonts:
            @import url("https://...");


            // E.g.
            body {
                font-family: $font-family;
                color: $body_color;
            }