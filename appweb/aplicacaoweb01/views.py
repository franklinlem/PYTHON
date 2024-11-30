from django.shortcuts import render
from django.urls import reverse
from .models import Topic
from .forms import TopicForm
from django.http import HttpResponseRedirect

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
    entries = topic.entry_set.order_by('-date_added') # type: ignore
    context = {'topic': topic, 'entries': entries}
    return render(request, 'aplicacaoweb01/topic.html', context)

def new_topic(request):
    """Adicionar novo tópico"""
    if request.method != 'POST':
        #Criar form em branco se nada for enviado
        form = TopicForm()
    else:
        #Criar form com dados enviados pelo usuário
        form = TopicForm(request.POST)
        if form.is_valid():
            #Salvar o novo tópico
            form.save()
            return topics(request)
            #return HttpResponseRedirect('/topics/')
            #return HttpResponseRedirect(reverse('topics'))
        
    context = {'form':form}        
    return render(request, 'aplicacaoweb01/new_topic.html', context)