
# RECOMMENDED APPROACH FOR GENERAL!
# Output in CMS: Django highlights the field and set a default error message over the field!
if not self.name:
    raise ValidationError(
        {
            "name": ValidationError(
                "",               # custom msg, but if you use it, comment the code arg!
                code="required"   # if code's called, no matter what custom msg, django uses default
                # More codes:
                # ./error-identification-codes.txt
            )
        }
    )



# RECOMMENDED ONLY FOR THOSE COMPLEX OR CROSS-FIELD VALIDATIONS:
# Output in CMS: Django highlights the field and set the custom error message over the field!
if not self.name:
    raise ValidationError(
        {
            "name": ValidationError(
                "This fucking field is required, bloody hell!",
                # code="required",  # Deactive this to use the custom message!
            )
        }
    )
