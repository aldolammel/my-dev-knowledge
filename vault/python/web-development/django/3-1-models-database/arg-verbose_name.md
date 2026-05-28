

DJANGO MODEL CLASS > ARGUMENT: VERBOSE_NAME

    >> It's possible to add a verbose name for each attribute but it is NOT database level.
            In the database, the column name will exactly be the attribute name as it is.

            E.g default label name will be the attribute name, converting each '_' in space:

                class Recipe(models.Model):
                    start_datetime = models.DateTimeField()

                output: 'Start Dateime'
                

    >> If you set a verbose name in a models.py class, it will be customized on Admin/CMS and
        the web application front-end:

            E.g. in models.py:

                class Recipe(models.Model):
                    start_datetime = models.DateTimeField(verbose_name='Start')


    >> Except if you customized your forms.py class where, in this case, the front-end will
        shown your attribute/field with another label:

            E.g. in forms.py:

                class RecipeForm(models.ModelForm):
                    class Meta:
                        labels = {
                            'start_datetime': 'When did it gets start?',
                        }