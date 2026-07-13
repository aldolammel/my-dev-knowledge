
# USED IN MODEL CLEAN() METHOD (FOR COMPLEX OR CROSS-FIELD VALIDATIONS):
# Result in CMS, e.g. Django highlights the field and set the custom warning message over the field!
if not self.fieldnamehere:
    raise ValidationError(
        {
            "fieldnamehere": ValidationError(
                "This field is required!",  
                # code="required",  # Deactive this to use the custom message! (Looks useless!!!!)
                    # More codes:
                    # ./error-identification-codes.md
            )
        }
    )

"""- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    IN DJANGO, VALIDATION-ERRORS ARE USED MAINLY THROUGH CLEAN() METHODS:
        - Clean for models: /python/web-development/django/3-1-models-database/method-clean.py
        - Clean for forms: /python/web-development/django/9-forms/method-clean.py
    
    MORE ABOUT PYTHON ERROR MESSAGES:
        /python/python-knowledge/errors/_errors-most-common.py

"""