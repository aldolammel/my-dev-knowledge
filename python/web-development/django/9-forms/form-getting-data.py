''' 

    FORMS: GETTING DATA

        >> Form gets data from Model;
        >> Form gets data from View;

    >> Sending data:
        ./form-sending-data.py
'''


# FROM MODEL TO FORM  - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# forms.py
class MovieForm(forms.ModelForm):

    class Meta:
        # Model tied used to populate it:
        model = models.Movie
        # Bringing specific fields from the model:
        # Django rule: to be called here, the field CANNOT be 'editable=False', nor custom method. If the field is editable but for the form it should be readonly_fields, no problem, call it!
        fields = [
            'title',  # field from Model;
            'director',  # field from Model;
            # 'director_gender',  # Just to create an example, let's imagine this field cannot be available in forms at all! Further, I'll show how to get this data!
            # 'year'  # Just to create one more example soon.
        ]

    def clean_title(self):
        # Once this form has in its 'fields' array the field 'title', you take the data like this:
        title = self.cleaned_data.get('title')  # Avoid to use cleaned_data['something'] 'cause if it fails it returns KeyError instead of None (safer).
        ...

    def clean_director(self):
        # As this individual clean() method is natively auto-waiting just 'director' field data, to get data from another field (including those NOT available as a field in form 'fields' array, you need to call directly the MODEL instance here. E.g.:
        director = self.cleaned_data.get('director') # Accepted once the clean is auto waiting it here!

        # Let's take what we need from the model instance directly:
        director_gender = (
            self.instance.director_gender
            if self.instance and self.instance.director_gender
            else None
        )
        # Condition to raise a warning message demanded by any clean() use:
        if not director and director_gender:
            raise forms.ValidationError("Director is not a required field, except if it got a gender.")
        
    def _what_is_the_year(self):
        # Another example showing how to get a unavailable data in form, using an internal custom form method to get the data straight from the tied Model!
        # E.g. calling it: year = self._what_is_the_year()
        return (
            self.instance.year
            if self.instance and self.instance.year
            else None
        )
    

# FROM VIEWS TO FORM - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# views.py
def movie_view(request, pk):

    # Defining the specific movie:
    movie = get_object_or_404(Movie, pk=pk)

    # If someone is sending a new movie or changes:
    if request.method == 'POST':

        # View must send this data to the movie-form on template:
        form = MovieForm(request.POST, instance=movie, user=request.user)
        ...

    # Otherwise, if it's just someone seeing the content:
    else:
        # Still, keep sending the data to the movie-form on template:
        form = MovieForm(instance=movie, user=request.user)

    # You can send more content through the Context too:
    context = {...}
    return render(request, 'movies/detail.html', context)