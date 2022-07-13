from django.shortcuts import render

from .models import Topic

def index(request):
    """The home page for todoapp"""
    return render(request, 'todoapps/index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'todoapps/topics.html', context)
