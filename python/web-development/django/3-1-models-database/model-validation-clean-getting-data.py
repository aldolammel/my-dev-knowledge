
"""
    DJANGO > MODEL > CUSTOM VALIDATIONS: USING CLEAN() TO GET DATA AND THEN VALIDATE IT
    
        >> Using clean() method in forms.py:
            /python/web-development/django/9-forms/form-validation-clean-getting-data.py

        >> Model clean() VS Form clean():
            /python/web-development/django/6-errors-and-validations/2-clean-differences-between-model-and-form.py
        
        >> I'm sure I wanna use clean() method in models.py:
            KEEP IN THIS FILE!
"""


# HOW TO GET DATA FROM A MODEL TO VALIDATE ITSELF STILL IN MODELS.PY - - - - - - - - - - - - - - - -
# /apps/my_app/models.py:

class ExampleModel(models.Model):

    id = ...
    title = ...

    def clean(self):
        """Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""

        # Once the clean() is applied directly as a method in the model, to call the model (instance) data from db, just use 'self' to refer data from the own instance:
        if self.title:
            ...

            # Unlike Form clean() method, the Model clean() returns nothing if no validation error, otherwise, it expects the 'raise ValidationError' usage:
            raise ValidationError(...)


# HOW TO GET DATA FROM ANOTHER MODEL TO VALIDATE THE CURRENT MODEL STILL IN MODELS.PY - - - - - - - 
# /apps/my_app/models.py:

class MyModelMoreData(models.Model):
    ...


class MyModel(models.Model):

    id = ...

    def clean(self):
        # Only for existent instances, ignoring new instances (because new ones has no id yet):
        if self.pk:
            # Check if there is data from another model:
            is_data_available = MyModelMoreData.object.filter(status='True').exists()
            if not is_data_available:
                raise ValidationError("Feedback error message here...")

        # In this example, you see I'm calling data from this model (MyModel) itself using 'self', and calling data from another model (MyModelMoreData) through a queryset.



# AN EXAMPLE OF EXTENSIVE USE OF QUERYSETS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# /apps/my_app/models.py:

class Event(models.Model):
    id = ...
    platform = ...
    event_type = ...
    event_title = ...

    def clean(self):
        # Case an event_title has the same name of other instance where the instance also has the same event_type and (if selected) the same platform, warn it:
        if self.event_title:

            # Filtering:
            qs_type = Event.objects.filter(
                event_title=self.event_title,
                event_type=self.event_type,
                platform=self.platform,
            ).exclude(pk=self.id)
            qs_plat = Event.objects.filter(
                event_title=self.event_title,
                platform=self.platform,
            ).exclude(pk=self.id)

            # Checking:
            if qs_type.exists():
                t = (
                    consts.STR_EVENT_TYPE_PLAT
                    if self.event_type == consts.INT_EVENT_TYPE_PLAT
                    else consts.STR_EVENT_TYPE_RDIO
                )
                raise ValidationError(f"This event already exists as {t}.")
            if qs_plat.exists():
                raise ValidationError(f"This event already exists for {self.platform}.")


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

