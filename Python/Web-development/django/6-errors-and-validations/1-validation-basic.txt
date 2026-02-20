

DJANGO: VALIDATIONS
    
    Let's talk about validations for Database, CMS, and for App itself (including Django Template). But first:
    
    When you read "Django Forms":

        The expression "Django Forms" refers to the form classes Django uses, including those in the admin (e.g., a new post form) and those used in the app’s front-end (e.g., a contact form). So, just to be clear, "Django Forms" mean Python classes (from django.forms) that handle rendering and validating user input. Django Forms represent:
        
        >> Forms in the Django CMS (yes, they use Django Forms);
        >> Forms in app's front-end (only if you're using Django's templating to create them);


    Files you'll use frequently:
    
        >> models.py:
            Empty file automatically created, it defines data models and database-level validation. Any validation here applies everywhere (CMS, front-end forms [if Django is the template solution too], serializers [APIs]), since it enforces business rules at the data layer. 
            NOT ANY validation approach configured in this file will protect data in db-level. But only here you are allowed to set db validations.
        
        >> admin.py: 
            Empty file automatically created, it customize the logic to be used on CMS through its list-views and detail-views. All validation created here, by overriding ModelAdmin methods (e.g. save_model, get_queryset, etc), will impact only forms used by the CMS.
            That said, you also can attached a customized form (from forms.py) to replace the original CMS form (detail-view) for a specific admin-class, extending the forms.py usage not only for app's front-end, but for the CMS as well.
        
        >> forms.py:
            Once you create this file, here is where you define forms that will be used through the app's front-end, and/or, if needed, used as custom CMS form.
            There are 2 cases of using forms from forms.py:

                1) Using '.ModelForm' based class: directly tied to a models.Model (common case);
                2) Using '.Form' based class: not tied to a model, useful for search bars, contact forms, filters, etc ('Django Template' as front-end solution is expected).

            For projects where Django Templates is not the front-end solution used, forms.py are restrict only to be used attached with admin-classes (CMS, via admin.py) or some API request, once the front-end forms are built/provided by another template framework (e.g. Vue, React, Angular).


    So, yes, you should set form validations through those 3 files but for different purposes your project demands:

        >> Creating basic and deepest validations directly in db (auto-propagates to CMS & APP too):
            ./validation-1-for-database.txt
        
        >> Creating customized validations for CMS level:
            ./validation-3-for-CMS-forms.txt

        >> Creating customized validation for APP level:
            ./validation-2-for-app-forms.txt

        >> Creating validation for all levels (Database + CMS + APP);
            ./validation-4-for-everywhere.txt
        

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


        >> Validations via MODELS.PY:
            ./2-clean-differences-between-model-and-form.py
        
        >> Validations via ADMIN.PY:
            The admin.py doesn't accept any kind of validation, except through a Modelform-class in forms.py! It doens't accept validation directly! Use forms.py!

        >> Validations via FORMS.PY:
            ./2-clean-differences-between-model-and-form.py


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
