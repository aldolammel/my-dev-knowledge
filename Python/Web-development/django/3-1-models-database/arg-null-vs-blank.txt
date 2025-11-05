

DJANGO MODEL CLASS > ARGUMENT: NULL vs BLANK

    >> 'blank=True' means the field is not mandatory (models are blank=False as default value).
        
    >> 'null=True' means, if the field is empty, in db the value is storage as 'null', not empty.

    >> If 'null=False', make sure you're using a 'default=' value in case of blank value.

    >> As exception, CharField and TextField the default value is an empty string ('') and
        'null=True' should be avoided.

    >> Avoid the redundance: e.g. CharField(blank=True, null=True)