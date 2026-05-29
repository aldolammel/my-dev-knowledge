

HOW TO DEFINE WHICH FORM FIELDS ARE REQUIRED AND WHICH OF THEM ARE NOT:


    class ExampleForm(forms.ModelForm):
        """
        <description of the form>
        """

        class Meta:
            ...

        def __init__(self, *args, **kwargs):
            """Dunder method called 'constructor' that runs automatically when a class instance is created."""
            super().__init__(*args, **kwargs)
            
            # These fields MUST be required:
            self.fields['sex'].required = True
            self.fields['birthdate'].required = True
            self.fields['country'].required = True
            
            # These fields must NOT be required:
            self.fields['city'].required = False
            self.fields['language'].required = False





        >> QUESTION: but isn't the 'blank=True' what defines whether a required field? 