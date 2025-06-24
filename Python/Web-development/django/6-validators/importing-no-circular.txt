

    IMPORTING WITH NO CIRCULAR IMPORT ISSUES:
        

        >> Direct imports (from .models import EventAttack) are preferable when there are no
            circular dependencies, as they make the code easier to read and follow.
            
        
        >> apps.get_model() is ideal for dynamic model loading and avoiding circular imports.


            E.g.

                from django.apps import apps

                <code...>

                <ModelClassName> = apps.get_model('subapp_name', 'ModelClassName')

                queryset_example = <ModelClassName>.objects.all()



                >> This way unfortunately the VSCode cannot notice the instance attributes without
                    to show as error:

                    E.g.

                        instance.created_by    <--- it's a real model class attribute but will be shown as 'not-defined'. 



        