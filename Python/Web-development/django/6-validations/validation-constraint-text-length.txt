

DJANGO FORM VALIDATIONS > DB CONSTRAINTS: TEXT WITH LENGTH CHECK

    INFO:
        In case Django prints out a "Unsupported lookup" for "length" or "length_range" error message during the migrate command, just register that lookup on models.py:

            from django.db.models.functions import Length
            models.CharField.register_lookup(Length)


    >> Ensure a txt field has minimum X characters amount - - - - - - - - - - - - - - - - - - - - - 

        class PagexCategory(models.Model):
            ...
            cat = models.CharField(...)

            class Meta:
                ...
                constraints = [
                    models.CheckConstraint(
                        condition=models.Q(cat__length__gte=3),
                        name="cat_min_length",
                    )
                ]


        WHAT WILL TAKE PLACE IN DB:

            ALTER TABLE pagex_category
            ADD CONSTRAINT cat_min_length
            CHECK (LENGTH(cat) >= 3);

    
    >> Ensure a txt field has minimum and maximum characters amount - - - - - - - - - - - - - - - - 
        
        class PagexCategory(models.Model):
            ...
            cat = models.CharField(...)

            class Meta:
                ...
                constraints = [
                    models.CheckConstraint(
                        condition=models.Q(cat__length__range=(consts.VAL_TITLE_MIN, consts.VAL_TITLE_MAX)),
                        name="cat_length",
                    ),
                ]


        WHAT WILL TAKE PLACE IN DB:

            ALTER TABLE pagex_category
            ADD CONSTRAINT cat_length 
            CHECK (LENGTH(cat) >= 3 AND LENGTH(cat) <= 100);