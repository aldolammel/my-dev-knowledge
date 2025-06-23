''' 

    FORMS: RECEIVING DATA (AND SENDING TOO)

        >> Forms receive data from Views and Models;
        >> Forms send data to Models;


'''

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


# FROM MODEL TO FORM  &  FROM FORM TO MODEL - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# forms.py
class MovieForm(forms.ModelForm):

    class Meta:
        # Connected model to populate:
        model = Movie
        # Ordering fields on the form:
        fields = [
            'title',  # field from Model;
            'director',  # field from Model;
        ]

    # Extra fields:
    # Reserved space...

    def __init__(self, *args, **kwargs):
        '''Built-in method that's called when the form is initializated.'''

        # Extracting the 'user' from the instance param/arg that view has sent:
        user = kwargs.pop('user', None)  # If no user, it'll be 'None'.
        super().__init__(*args, **kwargs)

        # Connected fields (from connected model), customizations:
        # Reserved space...

        # Extra fields, pre-populating:
        # Unlike fields from connected model, extra fields must be manually linked!
        # Reserved space...

    def save(self, user=None, commit=True):  # the save() is prepared to receive the 'user' too:
        '''Built-in method that, if triggered, create or update an instance in the connected model.'''

        # Defining the instance as all the form data collected, but without to save in db yet:
        instance = super().save(commit=False)
        # To save was authorized, so:
        if commit:
            # Pack all data from form:
            instance.save(user=user)
        # And finally, record the data (instance) in the connected model:
        return instance
