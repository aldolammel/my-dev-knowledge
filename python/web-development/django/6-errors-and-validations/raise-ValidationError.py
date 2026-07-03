
# RECOMMENDED APPROACH FOR GENERAL!
# Result in CMS: Django highlights the field and set the warning message over the field!
if not self.fieldnamehere:
    raise ValidationError(
        {
            "fieldnamehere": ValidationError(
                "This field is required!",  # custom msg, but if you use it, comment the code arg!
                # code="required"           # if code's called, no matter what custom msg, django uses default (Looks useless!!!!)
                    # More codes:
                    # ./error-identification-codes.md
            )
        }
    )



# RECOMMENDED ONLY FOR THOSE COMPLEX OR CROSS-FIELD VALIDATIONS:
# Result in CMS: Django highlights the field and set the custom error message over the field!
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