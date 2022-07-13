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

def topic(request, topic_id):
    """Show a single topic and all its tasks"""
    topic = Topic.objects.get(id=topic_id)
    tasks = topic.task_set.order_by('-date_added')
    context = {'topic': topic, 'tasks': tasks}
    return render(request, 'todoapps/topic.html', context)
