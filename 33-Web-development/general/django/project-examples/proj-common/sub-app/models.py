# For the example this file is not relevant!


class Recipe(models.Model):
    name = ...
    description = ...
    ingredients = ...

    def __str__(self):
        return self.name.capitalize()


"""
    MORE OPTIONS:
    /33-Web-development/general/django/3-1-backend-models-database/

"""
