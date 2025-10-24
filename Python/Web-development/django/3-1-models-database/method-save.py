

"""
    DJANGO MODELS > METHODS: SAVE()

    In short, the save() method in Django models.py persists model instances to the database. It creates a new record if the object doesn't exist yet, or updates an existing record if it does. So it does:

    - Creates new records or updates existing ones.
    - Works directly with database operations.
    - Called on model instances: my_object.save().

    >> Keep in mind:
    - Use save_model() for admin-specific logic that needs request context.
    - Use model's save() for business logic that should apply everywhere.
    - Use form's save() for form-specific data processing.

    >> The save() for Django Models is NOT the same of save() for Django Forms:
        /Python/Web-development/django/9-forms/method-save.py

    >> The save() for Django Admin Models is the save_model() method:
        /Python/Web-development/django/4-cms-admin/method-save_model.py
"""

# Structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Django automatically provides this save() method!
# But if you need override the original one, basic structure:
class ExampleModel(models.Model):
    #...
    def save(self, *args, **kwargs):
        """Built-in Model method that's executed when the db entry saving runs."""
        # custom save code...
        super().save(*args, **kwargs)


# Common example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    is_published = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        """Built-in Model method that's executed when the db entry saving runs."""
        # Auto-generate slug from title if not provided
        if not self.slug:
            self.slug = self.title.lower().replace(' ', '-')
        
        # Auto-update the updated_at timestamp
        self.updated_at = timezone.now()
        
        # Custom logic before publishing
        if self.is_published and not self.created_at:
            self.created_at = timezone.now()
        
        # Call the parent class save() to actually save to database
        super().save(*args, **kwargs)


# Using save() method in another model class method - - - - - - - - - - - - - - - - - - - - - - - - 

class ExampleModel2(models.Model):
    #...
    def a_custom_method(self):
        #...
        # Creates new record
        user = User(name="John", email="john@example.com")
        user.save()  # INSERT into database
        # Updates existing record
        user.name = "Jane"
        user.save()  # UPDATE database