

DJANGO FORMS: ERROR MESSAGES


    >> Error messages on Django template:
        .../django/3-3-frontend-templates/form-error-messages.html
        .../django/3-3-frontend-templates/form-error-css-customization.txt
    
    
    >> But learn the basic:
        .../django/6-errors-and-validations/1-validation-basic.txt
        .../django/6-errors-and-validations/2-clean-differences-between-model-and-form.py
        .../django/6-errors-and-validations/3-error-messages.txt

    
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    WIP:

    >> (WIP) Model argument 'error_messages={}' (server-side checking):

        It's the most reliable and solid way to ensure that anything that causes an infraction 
        for a given attribute will generate the planned error message. However, this method is 
        server-side, that is, it's handled by the server and not by the client machine.

            <example here> xxxxxxxxxxxxxxxx


    >> Error messages on App and CMS front-end (client-side checking):

        It's a great way to validate fields without consuming server resources.

            >> Basic when Django is the back-end:
                .../django/6-errors-and-validations/validation-2-for-app-forms.txt
                .../django/6-errors-and-validations/validation-3-for-CMS-forms.txt

            >> Knowledge regarding error message feedbacks via final user app's front-end:

                >> Using Django Template:
                    .../django/3-3-frontend-templates/form-error-messages.html

                >> Using Vue:
                    /xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

                >> Using React:
                    /xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

                >> Using Angular:
                    /xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
