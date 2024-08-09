from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, DONE, DRAFT
from .forms import StepOneForm, StepTwoForm


def movie_list(request):
    context = {'movies': Movie.objects.all()}
    return render(request, 'sandbox/movies.html', context)


def movie_step_one(request, pk=None):
    has_data = False
    if pk:
        instance = get_object_or_404(Movie, pk=pk)
        has_data = True
    else:
        instance = Movie()

    # When it creates a new data in the database:
    if request.method == 'POST':
        # When Delete button is pressed:
        if 'del' in request.POST:
            instance.delete_instance()
            return redirect('sandbox:movie_list')

        # Define the form of the current form:
        form = StepOneForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save()
            return redirect('sandbox:movie_step_two', pk=instance.pk)
    # When it just take data from the database:
    else:
        form = StepOneForm(instance=instance)

    context = {
        'form': form,
        'has_data': has_data,
        'bt_submit': 'Next',
        'bt_draft': 'Save to finish later',
        'bt_cancel': 'Cancel',
        'bt_del': 'Delete',
    }
    return render(request, 'sandbox/movie_step_one.html', context)


def movie_step_two(request, pk):
    instance = get_object_or_404(Movie, pk=pk)
    # When it asks to create a new data in the database:
    if request.method == 'POST':
        # When Discard-Draft is pressed:
        if 'discard_draft' in request.POST:
            instance.delete_instance()
            return redirect('sandbox:movie_list')
        #
        form = StepTwoForm(request.POST, instance=instance)
        if form.is_valid():
            # It creates the model instance, but dont save it to the db yet:
            instance = form.save(commit=False)
            if 'save_draft' in request.POST:
                instance.status = DRAFT
            else:
                instance.status = DONE
            instance.save()
            return redirect('sandbox:movie_list')

    else:
        form = StepTwoForm(instance=instance)

    context = {
        'form': form,
        'bt_submit': 'Done',
        'bt_draft': 'Save to finish later',
        'bt_discard': 'Discard all',
    }
    return render(request, 'sandbox/movie_step_two.html', context)




"""
    MORE OPTIONS:
    /33-Web-development/general/django/3-2-backend-views/

"""