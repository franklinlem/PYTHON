from django.shortcuts import render
from django.urls import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
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

def new_entry(request, topic_id):
    """Acrescenta novas anotações"""
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST':
        #Criar form em branco se nada for enviado
        form = EntryForm()
    else:
        #Criar form com dados enviados pelo usuário
        form = EntryForm(data=request.POST)
        if form.is_valid():
            #Salvar a nova entrada
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            #return topic(request, topic_id)
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
            #return HttpResponseRedirect(f'/topics/{topic_id}/')

    context = {'topic': topic, 'form': form}
    return render(request, 'aplicacaoweb01/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edita entrada"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        #Criar form com dados da entrada atual
        form = EntryForm(instance=entry)
    else:
        #Criar form com dados enviados pelo usuário
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            #Salvar as alterações na entrada
            form.save()
            #return topic(request, topic.id)
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
            #return HttpResponseRedirect(f'/topics/{topic.id}/')
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'aplicacaoweb01/edit_entry.html', context)