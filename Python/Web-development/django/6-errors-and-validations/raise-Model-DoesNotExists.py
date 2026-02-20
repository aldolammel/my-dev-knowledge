
"""
    DJANGO > RAISE ERROR: USING MODEL-CLASS-DOES-NOT-EXIST

    This is a Django-generated exception class. Django automatically creates a DoesNotExist exception for every model.

    More Django 'raise' options:
        ./raise-error.txt

    Python native 'raise' options:
        /Python/python-knowledge/errors/_errors-most-common.py
"""

# models.py
class ExampleModel(...): # singleton
    ...


# Anywhere else
# Error if NO Pagex singleton:
obj = ExampleModel.objects.first()
if not obj:
    raise ExampleModel.DoesNotExist("The 'ExampleModel' doesn't exist.")















""" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        /xxxxxxxxxxxxxxxxxxxxxxx
"""