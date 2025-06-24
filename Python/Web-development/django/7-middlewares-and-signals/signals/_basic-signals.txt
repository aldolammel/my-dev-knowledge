

BASIC SIGNALS



    >> Open the sub-app file called 'app.py', and ensure that the signals are connected at the right
        time. The common practice is to import the signals module in the ready method of your
        sub-app's configuration class:

            from django.apps import AppConfig

            class SubAppNameConfig(AppConfig):
                ...
                name = 'sub_app_folder_name'

                def ready(self):
                    import sub_app_folder_name.signals