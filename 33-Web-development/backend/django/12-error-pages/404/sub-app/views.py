from django.shortcuts import get_object_or_404
from .models import ModelExample


def view_example(request, pk):
    # Not need to render() or redirect() to a page manually if you're using get_object_or_404()':
    user = get_object_or_404(ModelExample, pk=pk)
    # This will 'raise Http404()' the 404 error page automatically if no query is found, looking
    # also the 404.html file in the '/project_root/templates/' folder.
