from django import forms


# USING FORMS.FORM CLASS
# Reminder: forms.Form never inputs data in the database because it's not linked with a model class.


class ReviewForm(forms.Form):  # That 'Form' in the classname is a convention.
    user_name = forms.CharField(
        label='Your name',
        max_length=40,
        error_messages={
            'required': 'Name must not be empty.',
            'max_length': 'Enter with a shorter name.',
        },
    )
    review_text = forms.CharField(
        label='Your feedback',
        max_length=300,
        widget=forms.Textarea,
    )
    rating = forms.IntegerField(
        label='Your rating',
        min_value=1,
        max_value=5,
    )


# ON THE TEMPLATE / FRONT-END:
# /Python/Web-development/django/9-forms/based-class-Form/template.html


# VIEWS.PY TIP:
# For form classes in forms.py that won't use any models.py class, it's recommended to use
# 'FormView' inherit in its view in views.py file.
# /Python/Web-development/django/3-2-views-and-API/1-building-context/class-based/_view-class-form.txt
