from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """Página inicial(index)"""
    return render(request, 'aplicacaoweb01/index.html')

def topics(request):
    """Página dos Tópicos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'aplicacaoweb01/topics.html', context)

def topic(request, topic_id):
    """Assunto e suas entradas"""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'aplicacaoweb01/topic.html', context)