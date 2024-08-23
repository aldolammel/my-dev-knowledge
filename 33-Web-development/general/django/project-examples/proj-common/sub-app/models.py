# For the example this file is not relevant!


class Recipe(models.Model):
    name = ...
    description = ...
    ingredients = ...

    class Meta:
        db_table = 'recipe'
        ordering = ['name', '-description']
        # verbose_name = 'Recipe'
        # verbose_name_plural = 'Recipes'

    def __str__(self):
        return self.name.capitalize()

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        self.description = self.description.lower()
        self.ingredients = self.ingredients.lower()
        super().save(*args, **kwargs)


"""
    MORE OPTIONS:
    /33-Web-development/general/django/3-1-backend-models-database/

"""
