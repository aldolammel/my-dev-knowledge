

# BASIC VALIDATIONS:

'''
    >> All validations (created and build-in) work not only on CMS layer, but also on front-end
        and wherever the save() is used by python.
        
    >> Theses validations are never applied at database layer;
    
    >> Django has many built-in validators available:
        - MinValueValidator | MaxValueValidator
        - MinLengthValidator | MaxLengthValidator
        - EmailValidator | validate_email
        - FileExtensionValidator | validate_image_file_extension
        - URLValidator | validate_slug | validate_unicode_slug
        - validate_ipv4_address | validate_ipv6_address | validate_ipv46_address
        - int_list_validator | validate_comma_separated_integer_list
        - ProhibitNullCharactersValidator
        - StepValueValidator
        - DecimalValidator
        - RegexValidator
        
        More: https://docs.djangoproject.com/en/5.0/ref/validators/
        
'''

    # 1) XXXXXXXXXXXXXXXXX
        
        from django.core.validators import MinValueValidator, MaxValueValidator

        class Rating(models.Model):
            rating = models.PositiveSmallIntegerField(
                validators=[MinValueValidator(1), MaxValueValidator(5)]
            )
            
            def __str__(self):
                return f'Rating: {self.rating}'
            


    # 2) XXXXXXXXXXXXXXXXX



    # 3) XXXXXXXXXXXXXXXXX
        
    
    
    