

DJANGO MODEL CLASS > ATTRIBUTE TYPE: MANY-TO-MANY FIELD


    Common Usage:
        Defining a many-to-many relationship between two models. This requires Django to create a separate "junction" or "through" table in the database.


    Field look-like on front-end:
        xxxxxxx


    Example:
        
        categories = models.ManyToManyField(           # m2m attr name's an exception: always PLURAL
            "PagexCategory",
            blank=True,
            related_name="%(app_label)s_categories",                        # ./arg-related_name.txt
        )

        # On an Article model (an article can have many tags, and a tag can be on many articles):
        tags = models.ManyToManyField(Tag)

        # On a Course model (a student can take many courses, and a course can have many students):
        students = models.ManyToManyField(Student)



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


>> OTHER RELATED OPTIONS:
    
    >> Foreign Key:
        ./model-attr-foreignKey.txt

    >> One-To-One Field:
        ./model-attr-field-one-to-one.txt

