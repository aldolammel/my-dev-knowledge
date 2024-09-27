from django.shortcuts import render, get_object_or_404
from .models import ModelExample


def view_example(request, pk=None):
    if pk:
        instance = get_object_or_404(ModelExample, pk=pk)
        # Check if the id/pk is the same of the instance owner:
        if request.user != instance.created_by:
            return render(request, '401.html', status=401)

    # code...
