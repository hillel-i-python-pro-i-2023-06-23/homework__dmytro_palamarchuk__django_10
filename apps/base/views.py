"""View for the base application"""
from django.shortcuts import render

def hello_world(request):
    """Hello world"""
    content = 'Hello world'
    return render(request, 'index.html', {'content': content})