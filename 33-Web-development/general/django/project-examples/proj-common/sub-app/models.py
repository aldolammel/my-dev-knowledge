# For the example this file is not relevant!


class Recipe(models.Model):
    name = ...
    description = ...
    ingredients = ...
    
    def __str__(self):
        return self.name.capitalize()
