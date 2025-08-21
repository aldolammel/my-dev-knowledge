from django import forms
from .models import Review  # just for example (the model doesnt exist)


# USING FORMS.MODELFORM CLASS
# Reminder: forms.ModelForm links a form to the database through a previously created model class.
# Basically, the .ModelForm will take all model class (From models.py file) and recreate that
# automatically as a form on the template/front-end:


class ReviewForm(forms.ModelForm):  # That 'Form' in the classname is a convention.
    # Call this the built-in class:
    class Meta:
        # Defining with models.py class will be the model for this forms.py class:
        model = Review()
        # To show all fields declared in Review models.py class:
        fields = '__all__'
        # If you want to select with fields should be shown:
        # fields = ['review_text', 'rating']
        # If you want to show all, except one or other field:
        # exclude = ['user_name', 'owner_comment']
        # If you want to customize the form labels:
        labels = {
            'user_name': 'Your Name',
            'review_text': 'Your Review',
        }
        # Cutomizing the field/input features as well as its HTML attributes:
        widgets = {
            'review_text': forms.Textarea(
                attrs={
                    'placeholder': 'place_holder_text_here',
                    'class': 'my-css-class',
                    'rows': '5',
                }
            ),
        }
        # Customizing the error msgs for required fields:
        error_messages = {
            'user_name': {
                'required': 'xxxxxxxxxxxxxxxxx',
                'max_length': 'yyyyyyyyyyyyyy',
                'incomplete': 'nnnnnnnnnnnn',
            },
            'review_text': {
                'required': 'xxxxxxxxxxxxxxxxx',
                'max_length': 'yyyyyyyyyyyyyy',
                'incomplete': 'nnnnnnnnnnnn',
            },
            'rating': {
                'required': 'xxxxxxxxxxxxxxxxx',
                'max_length': 'yyyyyyyyyyyyyy',
                'incomplete': 'nnnnnnnnnnnn',
            },
        }


# ON THE TEMPLATE / FRONT-END:
# /Python/Web-development/django/9-forms/based-class-ModelForm/template.html
