from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.http import Http404
from .models import ModelExample


@login_required
def some_view(request, pk=None):

    # Check if some pk was provided:
    if pk:
        # Check if the provided pk exists:
        try:
            # Defining the specific instance:
            instance = get_object_or_404(ModelExample, pk=pk)
        except Http404:
            return redirect('general:404_view')
    
    # code...