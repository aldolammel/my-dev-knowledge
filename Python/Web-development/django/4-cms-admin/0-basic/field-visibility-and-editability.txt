

FIELD VISIBILITY AND EDITABILITY:

    Which Admin field feature to develop:

    A) Visible but locked (not editable);
    B) Completely hidden (in List View and Detail View);
    C) Partialy hidden, visible only in List View;
    D) Partialy hidden, visible only in Detail View;
    E) Context visibility and editability, only if another option is chosen;

    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    A) VISIBLE BUT LOCKED (NOT EDITABLE)

        >> If you want to make a specific field visible but also locked in the CMS detail view, 
            unable for manual changes, do it:

            A.1) In 'admin.py', create or edit the class related with the original models.py class, 
                including:

                    E.g.
                        class ExampleClassCMS(admin.ModelAdmin):
                            readonly_fields = ('<field_you_wanna_lock>',)

                        admin.site.register(ExampleClass, ExampleClassCMS)


                Important: if that specific attribute in your 'models.py' class is using 
                            'editable=...' argument, the editable value (True or False) will be
                            ignored by your CMS;


    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    B) COMPLETELY HIDDEN


        >> If you want to make a specific field invible in the entire CMS, do it:

            B.1) In 'models.py', go to the right class and its specific attribute;
            B.2) In the attribute arguments, add or edit the 'editable':

                    E.g.
                        class ExampleClass(models.Model):
                            attrib_example = models.CharField(editable=False)

            B.3) In 'admin.py', make sure the attribute that must be hidden is NOT in the 
                list_display:

                    E.g.
                        class ExampleClassCMS(admin.ModelAdmin):
                            list_display = ('<the_field_shouldnt_be_here>',)


    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    C) PARTIALY HIDDEN: VISIBLE ONLY IN LIST VIEW

        >> If you want to make a specific field visible in CMS List View but NOT in Detail View:

            C.1) In 'models.py', go to the right class and its specific attribute;
            C.2) In the attribute arguments, add or edit the 'editable':

                    E.g.
                        class ExampleClass(models.Model):
                            attrib_example = models.CharField(editable=False)

            C.3) In 'admin.py', make sure the attribute that must be hidden is in the list_display:

                    E.g.
                        class ExampleClassCMS(admin.ModelAdmin):
                            list_display = ('<the_field_must_be_here>',)

    
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    D) PARTIALY HIDDEN: VISIBLE ONLY IN DETAIL VIEW

        >> If you want to make a specific field visible in CMS Detail View but NOT in List View:

            D.1) In 'models.py', go to the right class and its specific attribute;
            D.2) In the attribute arguments, edit as 'True' the 'editable' or remove the arg. 
                completely:

                    E.g.
                        class ExampleClass(models.Model):
                            attrib_example = models.CharField()
            
            D.3) In 'admin.py', if there's the related admin class for the original models.py class, 
                make sure the attribute that must be hidden in CMS List View is NOT listed:

                    E.g.
                        class ExampleClassCMS(admin.ModelAdmin):
                            list_display = ('<the_field_shouldnt_be_here>',)


    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    E) CONTEXT VISIBILITY AND EDITABILITY: ONLY IF ANOTHER OPTION IS CHOSEN

        >> If you want to make a specific field visible and unlocked in CMS only if another field
            with a specific value is chosen, and clean and lock the same field if another else is
            chosen:

            E.1) In model class (in models.py) that has those fields to consider, add or edit
                the save() method to force the cleaning when needed:

                E.g.
                    def save(self, *args, **kwargs):
                        # Runs full validation before saving:
                        self.full_clean()
                        # Reset <field_to_clean_and_lock> if <reason>:
                        if self.<another_field> condition:
                            self.<field_to_clean_and_lock> = None

                        return super().save(*args, **kwargs)

            E.2) Now, go to the admin.py, and, in the admin class related of the changed model class,
                add or edit get_fields() and get_readonly_fields() methods: 

                E.g.
                    def get_fields(self, request, obj=None):
                    """Dynamically control which fields from this class are shown in the CMS."""
                    fields = ['<another_field>']
                    if obj and obj.<another_field> condition:
                        fields.append('<field_to_clean_and_lock>')
                    return fields
                
                    def get_readonly_fields(self, request, obj=None):
                        """Lock <field_to_clean_and_lock> if <another_field> condition."""
                        if obj and obj.<another_field> condition:
                            return ['<field_to_clean_and_lock>']
                        return []

           