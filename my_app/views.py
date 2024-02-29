from django.shortcuts import render
from django.views import generic

class HomePage(generic.TemplateView):
    """
    Displays hero image and cards section with login/about
    links on landing page.
    """
    template_name = 'index.html'
