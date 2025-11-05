

DJANGO MODEL CLASS > ARGUMENT: AUTO_NOW_ADD vs AUTO_NOW

    >> 'auto_now_add=True' means when a new instance/entry is created in the table, the attribute
            will be filled automatically once.

            E.g. created_at = models.DateTimeField(auto_now_add=True)
    
    >> 'auto_now=True' means when an instance/entry is modified, the attribute will be updated
        automatically.

            E.g. updated_at = models.DateTimeField(auto_now=True)