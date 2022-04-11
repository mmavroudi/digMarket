from django.shortcuts import render, get_object_or_404


def home_view(request, template_path='home.html'):
    """
    Markeplace home
    """
    context = dict()
    return render(request, template_path, context)
