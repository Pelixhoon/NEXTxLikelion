from django.shortcuts import render
from .models import Todo
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    lists = Todo.objects.all().order_by('deadline')

    return render(request, 'home.html', {'lists':lists})

def new(request):
    if request.method == 'POST':
        new_list = Todo.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline']
        )
        return redirect('detail', new_list.pk)
    
    return render(request, 'new.html')

def detail(request,	list_pk):
    list = Todo.objects.get(pk=list_pk)

    return render(request, 'detail.html', {'list':list})

def edit(request, list_pk):
    list = Todo.objects.get(pk=list_pk)

    if request.method == 'POST':
        Todo.objects.filter(pk=list_pk).update(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail', list_pk)

    return render(request, 'edit.html', {'list':list})

def delete(request,	list_pk):
    list= Todo.objects.get(pk=list_pk)
    list.delete()
    
    return redirect('home')