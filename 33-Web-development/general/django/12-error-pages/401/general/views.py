from django.shortcuts import render


def error_401(request):
    # context = {}
    return render(request, 'general/401.html')
