

"""
    DJANGO MODELS > METHODS: CREATE A CUSTOM METHOD BY YOUR OWN

    Create custom methods to use inside or outside the class.

    For not custom one, e.g. of a built-in method:
        ./method-clean.py

"""

# Structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

class ExampleModel(models.Model):
    ...

    # Built-in method should come first, e.g.:
    def clean(self):
        pass

    # In the bottom of the list, set your custom methods:
    def _my_custom_internal_method(self):
        """Convention: this '_' prefix means it should be used only for other methods in the class."""
        return something

    def my_custom_method(self):
        """Convention: Without '_' means this method can be used everywhere."""
        return something