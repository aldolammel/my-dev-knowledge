

DJANGO FORM VALIDATIONS > DB CONSTRAINTS > DATE: PROTECTING DATE LOGIC


    >> Start-Date must be before or, at least, equal to End-Date - - - - - - - - - - - - - - - - - -
    
        # FILE: /apps/my_app/models.py
        from django.db import models

        class Event(models.Model):
            ...
            start_date = models.DateTimeField()
            end_date = models.DateTimeField()

            class Meta:
                constraints = [
                    models.CheckConstraint(
                        condition=models.Q(start_date__lte=models.F("end_date")),
                        name="start_before_end",
                    )
                ]


        WHAT WILL TAKE PLACE IN DB:
        
            ALTER TABLE "event"
            ADD CONSTRAINT "start_before_end"
            CHECK ("start_date" <= "end_date");



    >> Other date example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        xxxxxx

        WHAT WILL TAKE PLACE IN DB:

            xxxxxxxxx

---
## Other db-level constraint types:
[/python/web-development/django/6-errors-and-validations/validation-1-for-database](/python/web-development/django/6-errors-and-validations/validation-1-for-database.md)
## This constraint type on SQL:
[/database/constraint-type-check](/database/constraint-type-check.md)

