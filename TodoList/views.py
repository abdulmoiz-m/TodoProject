from django.shortcuts import render, redirect
from .models import Todo
from .forms import TaskForm


# Create your views here.
def index(request):
    tasks = Todo.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def add(request):
    form = TaskForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('show_tasks')

    context = {'form': form}
    return render(request, 'add.html', context)


def update(request, task_id):
    task = Todo.objects.get(id=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('show_tasks')

    context = {'form': form}
    return render(request, 'update.html', context)


def delete(request, task_id):
    task = Todo.objects.get(id=task_id)
    if request.method == 'GET':
        task.delete()
    return redirect('show_tasks')


def search(request):
    search_term = request.GET.get('search-term') or ''
    searched_tasks = Todo.objects.filter(task_name__icontains=search_term)
    context = {'tasks': searched_tasks}

    return render(request, 'index.html', context)
