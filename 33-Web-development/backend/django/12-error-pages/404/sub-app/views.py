from django.shortcuts import get_object_or_404
from .models import ModelExample


def view_example_1(request, pk):
    # Not need to render() or redirect() to a page manually if you're using get_object_or_404()':
    user = get_object_or_404(ModelExample, pk=pk)
    # This will 'raise Http404()' the 404 error page automatically if no query is found, looking
    # also the 404.html file in the '/project_root/templates/' folder.


def view_example_2(request, pk):
    ...
    return render(request, '404.html', status=404)



"""
PATH:

If the file is only 'file_name.html' it means the html file is alocated
in /project/templates/file_name.html.

If you need to call a file from an sub-app folder:

Right way:
'sub-app/file_name.html', it doens't need to explicit set 'templates' folder.

Bad way:
'sub-app/templates/file_name.html'

"""
