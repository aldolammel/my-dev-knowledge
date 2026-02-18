


    NAMESPACE: WHERE TO USE SAFELY

    A few examples how to use the app name as constants.



    >> settings.py:

        E.g.

            INSTALLED_APPS = [
                ...,
                # APP ORIGINAL SUB-APPS:
                "apps." + NAMEAPP_1,
                "apps." + NAMEAPP_2,
                "apps." + NAMEAPP_3,
                ...
            ]



    >> apps.py:

        E.g.

            from django.apps import AppConfig
            from cefalog.consts import NAMEAPP_3


            class AccountsConfig(AppConfig):  <----------------------- NEVER CHANGE THIS CLASS NAME!
                default_auto_field = 'django.db.models.BigAutoField'
                name = "apps." + NAMEAPP_3

                def ready(self):
                    import accounts.signals   <----------------------- NEITHER!



    >> views.py:

        E.g.

            if request.method == 'POST':
                if 'del_account' in request.POST:
                    instance.delete_instance()
                    return redirect(NAMEAPP_1 + ':' + PATTERN_1_1)




    >> Etc...