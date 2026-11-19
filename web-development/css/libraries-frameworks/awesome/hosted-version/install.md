

    FONT-AWESOME: INSTALLING WITHIN THE PROJECT

        1) Download the package: https://fontawesome.com/ 


        2) Copy both the '/webfonts' and the '/css' folders into your project’s static assets
            directory:

                E.g.

                    /static/fontawesome/
                    /static/fontawesome/css/
                    /static/fontawesome/webfonts/


        3) Reference Font Awesome in Your Project: Link the core fontawesome.css file along with 
            the CSS files for whichever styles you want to use into the <head> of each template 
            or page that you plan to add icons to:

                E.g.

                    <head>
                        <!-- core file -->
                        <link href="/your-path-to-fontawesome/css/fontawesome.css" rel="stylesheet" />
                        <!-- style ones -->
                        <link href="/your-path-to-fontawesome/css/brands.css" rel="stylesheet" />
                        <link href="/your-path-to-fontawesome/css/solid.css" rel="stylesheet" />
                    </head>
                    <body>
                        <i class="fa-solid fa-user"></i>
                        <i class="fa-brands fa-github-square"></i>
                    </body>


        4) That's it! Test it!