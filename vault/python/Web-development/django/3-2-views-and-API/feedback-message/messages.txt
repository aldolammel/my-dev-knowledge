

    FEEDBACK MESSAGES:

        >> xxxxxxxxxxxxxx



        from django.contrib import messages




        messages.debug(request, "%s SQL statements were executed." % count)
        messages.info(request, "Three credits remain in your account.")
        messages.success(request, "Profile details updated.")
        messages.warning(request, "Your account expires in three days.")
        messages.error(request, "Document deleted.")