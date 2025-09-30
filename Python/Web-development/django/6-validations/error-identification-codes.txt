

>> code='invalid':
                
    Meaning that the provided data is not valid according to the specified
    rules.


>> code='required':

    Raised when a required field is left empty.


>> code='unique': 

    Raised when a field or model requires unique values, and the user submits a
    duplicate value.


>> code='max_length' | code='min_length':

    Max - Raised when the length of the input exceeds the maximum allowed length
            for a field.
    
    Min - Raised when the length of the input is less than the minimum required
            length for a field.  


>> code='max_value' | code='min_value':

    Max - Raised when the value of a numeric field exceeds the maximum
            allowable value.
    
    Min - Raised when the value of a numeric field is below the minimum
            allowable value.


>> code='invalid_choice':

    Raised when a value is selected that is not a valid choice for
    a ChoiceField.


>> code='overlap':

    Custom error code when two fields have overlapping or conflicting values
    (useful in date ranges, or two ChoiceField selected options conflicting).


>> code='non_field_error':

    This is a catch-all error code used for validations that don't belong to
    a specific field, such as cross-field validations (conflicting).


>> code='blank' | code='null':

    blank - Raised when a required field is left blank, even though null might
            be allowed at the database level, but blank=False for forms.

    null - Raised when a field value is None but the field does not allow null
            values (null=False in a model).


>> code='permission_denied':

    Raised when the user doesn't have permission to perform a certain action.


>> code='invalid_login':

    Raised when login credentials (username/password) are incorrect.

