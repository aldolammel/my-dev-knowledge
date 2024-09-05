from django.shortcuts import render


def error_404(request):
    # context = {}
    return render(request, 'general/404.html')
