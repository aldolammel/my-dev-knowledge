

CREATING AN EXPLICIT ID/PK:

    
    >> In Django, Primary-Keys are created automatically by default, so Django creates a field
        called 'id' for each Model Class you created if you don't declarate that explicitly.

        
    >> Defining it by your own:

        E.g.
            class Movie(models.Model):
                id = models.AutoField(primary_key=True)  # 'id' arg/param can be customized too!

    
    >> Your options:
    
        .SmallAutoField ............ guaranteed to fit numbers from 1 to 32767.

        .AutoField ................. guaranteed to fit numbers from -2147483648 to 2147483647.

        .BigAutoField .............. guaranteed to fit numbers from 1 to 9223372036854775807.
        
        .UUIDField ................. Faster and more secure, but the db won't generate it for you,
                                    so it's recommended to use default:

                                        # In models.py:
                                        import uuid

                                        # In the model-class:
                                        id = models.UUIDField(
                                            primary_key=True, 
                                            default=uuid.uuid4, 
                                            editable=False
                                        )
