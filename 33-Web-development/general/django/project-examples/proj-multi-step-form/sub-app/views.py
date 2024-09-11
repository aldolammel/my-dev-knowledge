from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import StepOneForm, StepTwoForm


# CONSTANTS:
BT_NEXT = 'Next step'
BT_DISCARD = 'Discard this movie'
BT_DONE = 'Done'
BT_DRAFT = 'Save to finish later'
BT_CANCEL = 'Cancel'
BT_BACK = 'Previous step'


class MoviesListView(ListView):
    """
    Responsible for showing the movies list on the front-end.
    """

    model = Movie
    template_name = 'movies/list.html'
    context_object_name = 'movies'


def step_one(request, pk=None):
    # Initial values:
    title = 'Adding movie'

    # Check if some pk was provided:
    if pk:
        # Defining the specific instance:
        instance = get_object_or_404(Movie, pk=pk)
        # Defining page title:
        title = f'{instance.name} (Movie ID: {instance.pk})'
    else:
        instance = Movie()

    # When the form wants to change some in the database:
    if request.method == 'POST':
        # When user wants to delete the instance:
        if 'discard' in request.POST:
            instance.delete_instance()
            return redirect('movies:list_view')
        # Defining the object of the current form:
        form = StepOneForm(request.POST, instance=instance)
        if form.is_valid():
            #
            if 'save_draft' in request.POST:
                # It creates the model instance, but dont save it to the db yet:
                instance = form.save(commit=False)
                # Pass the logged-in user to the save method
                instance.save(user=request.user)
                return redirect('movies:list_view')
            else:
                # Pass the logged-in user to the save method
                instance = form.save(user=request.user)
                return redirect('movies:step_two_view', pk=instance.pk)
    # When the form doesn't change any (GET method):
    else:
        form = StepOneForm(instance=instance)

    # Defining what will be sent to the front-end/template:
    context = {
        'page_title': title,
        'form': form,
        'instance_pk': instance.pk,
        'bt_submit': BT_NEXT,
        'bt_draft': BT_DRAFT,
        'bt_back': BT_CANCEL,
        'bt_discard': BT_DISCARD,
    }
    # Load the template:
    return render(request, 'movies/step_one.html', context)


def step_two(request, pk):
    # Defining the specific instance:
    instance = get_object_or_404(Movie, pk=pk)
    # Check if the logged-in user is the owner of the instance:
    if request.user != instance.created_by:
        return render(request, 'general/401.html')
    # Defining page title:
    title = f'{instance.name} (Movie ID: {instance.pk})'

    # When the form wants to change some in the database:
    if request.method == 'POST':
        # When user wants to delete the instance:
        if 'discard' in request.POST:
            instance.delete_instance()
            return redirect('movies:list_view')
        #
        form = StepTwoForm(request.POST, instance=instance)
        if form.is_valid():
            #
            if 'save_draft' in request.POST:
                # It creates the model instance, but dont save it to the db yet:
                instance = form.save(commit=False)
                # Pass the logged-in user to the save method
                instance.save(user=request.user)
            else:
                # Pass the logged-in user to the save method
                instance.save(user=request.user)
                return redirect('movies:list_view')
    # When the form doesn't change any (GET method):
    else:
        form = StepTwoForm(instance=instance)

    # Defining what will be sent to the front-end/template:
    context = {
        'page_title': title,
        'form': form,
        'instance_pk': instance.pk,
        'bt_back': BT_BACK,
        'bt_submit': BT_DONE,
        # 'bt_draft': BT_DRAFT,
        'bt_discard': BT_DISCARD,
    }
    # Load the template:
    return render(request, 'movies/step_two.html', context)


"""
    MORE OPTIONS:
    /33-Web-development/general/django/3-2-backend-views/

"""
