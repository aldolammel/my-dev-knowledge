
AUTOFILL FIELD: COMPOSED FIELD

    Field = 'name'
    Field = 'lastname'
    Composed field = 'name' + 'lastname'

    >> Composed field allows you to build an attribute (column) automatically,
        join two or more attributes to create another one.


    1) Add in the class/table an attribute not editable:

        class Person(models.Model):
            fname = models.CharField(max_length=10)
            lname = models.CharField(max_length=10)
            full_name = models.CharField(max_length=60, editable=False)

    
    2) Now, in the same class, override the built-in save() method with the
        instruction about how to build the 'full_name' attribute before
        to save all data to the database:

            def save(self, *args, **kwargs):
                # Runs full validation before saving:
                self.full_clean()
                self.full_name = f'{self.fname} {self.lname}'
                super().save(*args, **kwargs)


    3) In the admin.py file, you have 3 approaches, depending of your goal:

        3.1) If you want to show the 'full_name' field but keep it unavailable
            for edition, do it:

                class PersonCMS(admin.ModelAdmin):
                    # Locks the field on the detail-view:
                    readonly_fields = ('full_name',)

        
        3.2) If you want to hide the 'full_name' field on the detail-view and 
            making it be shown on the list-view, do it:

                class PersonCMS(admin.ModelAdmin):
                    # Includes the field as a column on the list-view:
                    list_display = ('id', 'full_name')
                    # But excludes the field from the detail-view:
                    exclude = ('full_name',)

        3.3) If you want to hide the 'full_name' field completely, leaving it
            available only in the database, do it:

                class PersonCMS(admin.ModelAdmin):
                    exclude = ('full_name',)


        >> Make sure you're registering the admin class also:
        admin.site.register(Person, PersonCMS)
        

    4) Execute the commands to prepare the database and test the CMS:
        
        $ python manage.py makemigrations
        $ python manage.py migrate
        $ python manage.py runserver
        
        http://127.0.0.1:8000/admin/

