

DJANGO MODEL CLASS > ATTRIBUTE TYPE: FOREIGN KEY (NOT-FIELD)


    Common Usage:
        Defining a many-to-one relationship between two models. It creates a database foreign key from one table to another's primary key.


    Field look-like on front-end:
        Depends of the foreign field (ForeignKey) type!

    
    Example:

        from django.conf import settings as stgs
        
        # BlogPost model where many posts can be owned just by one author:
        created_by = models.ForeignKey(
            stgs.AUTH_USER_MODEL,
            editable=False,
            related_name="posts",
            on_delete=models.SET_NULL,
            null=True,
        )


        # The same, but only logic:
        <AttrOfModelA> = models.ForeignKey(
            <ModelB>,                                      # or between quotes if model comes later!
            editable=False,
            related_name="<WhatExactlyModelBownedHere+s>",                  # ./arg-related_name.txt
            on_delete=models.SET_NULL,
            null=True,
        )



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


>> OTHER RELATED OPTIONS:
    
    >> Many-To-Many Field:
        ./model-attr-field-many-to-many.txt



    