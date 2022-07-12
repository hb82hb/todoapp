from django.shortcuts import render

def index(request):
    """The home page for todoapp"""
    return render(request, 'todoapps/index.html')
