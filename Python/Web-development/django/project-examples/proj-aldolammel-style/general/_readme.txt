This sub-app must be used to set all sections and features that doesn't need an authenticated user, 
doesn't fit any specialized sub-app, and are not system pages.

E.g. of /general/ content:

    - common home page for all;
    - simple contact form page;
    - search result page;
    - privacy policy page;



What's looks like 'general', but it's not:


    Specialized sub-apps:
    (those without log-in needs)

        - blog


    System pages:
    (must be alocated in the global templates folder)

        - error pages (401)
        - global includes;
        - base.html



ABCOO:
@aldolammel