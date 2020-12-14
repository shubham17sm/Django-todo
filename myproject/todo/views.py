from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

def index_view(request):
    todo = Todo.objects.order_by("timestamp")
    context = {
        'todo': todo
    }
    return render(request, "base.html", context)


def add_task(request):
    if request.method == "POST":
        task = request.POST["task-item"]
        task_item = Todo()
        task_item.task = task
        task_item.save()
    
    return redirect('index')

def delete_task(request, pk):
    Todo.objects.get(pk=pk).delete()

    return redirect('index')


def delete_all_tasks(request):
    Todo.objects.all().delete()

    return redirect('index')


def complete_task(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.complete = True
    todo.save()

    return redirect('index')


def delete_all_complete(request):
    Todo.objects.filter(complete=True).delete()

    return redirect('index')


