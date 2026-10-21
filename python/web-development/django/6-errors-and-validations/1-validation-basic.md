#### Python > Django
# Validations

---
    
Let's talk about validations for Database, CMS, and for App itself (including Django Template). But first:
### When you read "Django Forms"
The expression *Django Forms* refers to the form classes Django uses, including those in the admin (e.g., a new post form) and those used in the app’s front-end (e.g., a contact form). So, just to be clear, *Django Forms* mean Python classes (from `django.forms`) that handle rendering and validating user input. Django Forms represent:
       
- Forms in the Django CMS (yes, they use *Django Forms*);
- Forms in app's front-end (only if you're using Django's templating to create them);

---
## Files you'll use frequently:
### `models.py`
Empty file automatically created, it defines data models and db-level validation. Any validation here applies everywhere (CMS, front-end forms \[if Django is the template solution too], serializers \[APIs]), since it enforces business rules at the data layer. NOT ANY validation approach configured in this file will protect data in db-level, **but only here you are allowed to set db validations.**
### `admin.py`
Empty file automatically created, it customize the logic to be used on CMS through its list-views and detail-views. All validation created here, by overriding ModelAdmin methods (e.g. `save_model()`, `get_queryset()`, etc), will impact only forms used by the CMS. That said, you also can attached a customized form (from `forms.py`) to replace the original CMS form (detail-view) for a specific admin-class, extending the `forms.py` usage not only for app's front-end, but for the CMS as well.
### `forms.py`
Once you manually create this file, here is where you define forms that will be used through the app's front-end, and/or, if needed, used as custom CMS form. There are 2 cases of using forms from `forms.py`:

- Using `.ModelForm` based class: directly tied to a `models.Model` (common case);
- Using `.Form` based class: not tied to a model, useful for search bars, contact forms, filters, etc (*Django Template* as front-end solution is expected).

For projects where Django Templates is not the front-end solution used, `forms.py` are restrict only to be used attached with admin-classes (CMS, via `admin.py`) or some API request, once the front-end forms are built/provided by another template framework (e.g. Vue, React, Angular).

---
## Validations through those 3 files:
So, yes, you should set form validations through those 3 files, but for different purposes your project demands:

- Creating basic and deepest validations directly in db (auto-propagates to CMS & APP too): [/python/web-development/django/6-errors-and-validations/validation-1-for-database](/python/web-development/django/6-errors-and-validations/validation-1-for-database.md)
- Creating customized validations for CMS level: [/python/web-development/django/6-errors-and-validations/validation-3-for-CMS-forms](/python/web-development/django/6-errors-and-validations/validation-3-for-CMS-forms.md)
- Creating customized validation for APP level: [/python/web-development/django/6-errors-and-validations/validation-2-for-app-forms](/python/web-development/django/6-errors-and-validations/validation-2-for-app-forms.md)
- Creating validation for all levels (Database + CMS + APP): [/python/web-development/django/6-errors-and-validations/validation-4-for-everywhere](/python/web-development/django/6-errors-and-validations/validation-4-for-everywhere.md)

---
## Validations via `models.py` and `forms.py`:
[/python/web-development/django/6-errors-and-validations/2-clean-differences-between-model-and-form](/python/web-development/django/6-errors-and-validations/2-clean-differences-between-model-and-form.md)
## Validations via `admin.py`:
The `admin.py` doesn't accept any kind of validation, except through a **Modelform-class** in `forms.py`. It doesn't accept validation directly! Use `forms.py`!

---
## Recommended approach by common validation case:

| Situation                                                                  | Recommended approach                                                                                                                                                                                                              | Affected level |
| -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| A field is required                                                        | [Model field configuration](/python/web-development/django/3-1-models-database/arg-null-vs-blank.md)                                                                                                                              | App + DB       |
| A field must be greater than zero                                          | [CheckConstraint()](/python/web-development/django/6-errors-and-validations/validation-constraint-numerical-logics.md)                                                                                                            | App + DB       |
| A value must be within a range                                             | [Validators](/python/web-development/django/6-errors-and-validations/models-validators-built-in.md) and/or [CheckConstraint()](/python/web-development/django/6-errors-and-validations/validation-constraint-numerical-logics.md) | App and/or DB  |
| A value must follow a specific format                                      | [Validators](/python/web-development/django/6-errors-and-validations/models-validators-built-in.md)                                                                                                                               | App            |
| A field must have a minimum or maximum length                              | Field args (`min_length` / `max_length`) and [Validators](/python/web-development/django/6-errors-and-validations/models-validators-built-in.md)                                                                                  | App + DB       |
| A single field must be unique                                              | [unique=True](/python/web-development/django/6-errors-and-validations/validation-constraint-uniqueness.md)                                                                                                                        | App + DB       |
| A combination of fields must be unique                                     | [UniqueConstraint()](/python/web-development/django/6-errors-and-validations/validation-constraint-uniqueness.md)                                                                                                                 | App + DB       |
| A field's value depends on another field's value                           | [*clean()* or form validation](/python/web-development/django/6-errors-and-validations/2-clean-differences-between-model-and-form.md), depending on the rule                                                                      | App            |
| Several fields must satisfy a business rule together                       | [Model clean()](/python/web-development/django/3-1-models-database/method-clean.md)                                                                                                                                               | App            |
| A drop-down must show only matching things                                 | [QuerySet filtering in the form](/python/web-development/django/9-forms/form-queryset-filtering-dropdown.md) or API                                                                                                               | App            |
| A drop-down must exclude an instance when it's self-referential            | [QuerySet filtering in the form](/python/web-development/django/9-forms/form-queryset-filtering-dropdown.md) or API                                                                                                               | App            |
| A string must be normalized before validation (e.g., lowercase always)     | [Normalize the value](/python/web-development/django/3-1-models-database/controlling-the-capitalization.md), then validate it                                                                                                     | App            |
| A field must be unique regardless of capitalization                        | [UniqueConstraint()](/python/web-development/django/6-errors-and-validations/validation-constraint-uniqueness.md) with [Lower()](/python/web-development/django/3-1-models-database/controlling-the-capitalization.md)            | App + DB       |
| A field must be unique only when a condition is met (e.g., active records) | [Conditional UniqueConstraint()](/python/web-development/django/6-errors-and-validations/validation-constraint-conditionals.md)                                                                                                   | App + DB       |


