from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

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

def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # POST data submitted; process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('todoapps:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'todoapps/new_topic.html', context)
