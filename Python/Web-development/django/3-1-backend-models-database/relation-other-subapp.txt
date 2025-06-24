

RELATION: OTHER SUB-APP


    >> Relationships with other apps and their models (built-in or custom apps):

        class Review(models.Model):
            ...
            product = models.ForeignKey('store.Product')  # '<appname>.<modelname>'

            >> You can reference models defined in other Django apps (no matter if created by you,
            via python manage.py startapp <appname> or if it's a built-in or third-party app) by using
            the app name and then the name of the model inside the app.