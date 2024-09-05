from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .models import ModelExample


@login_required
def step_when(request, pk=None):

    # Checking if there's data:
    if pk:
        # Defining the specific instance:
        instance = get_object_or_404(ModelExample, pk=pk)
        # Check if the logged-in user is the owner of the instance:
        if request.user != instance.created_by:
            return redirect('general:401_view')
    else:
        instance = ModelExample()

    # code...
