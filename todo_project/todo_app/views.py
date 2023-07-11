from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_manager(request):
    tasks = Task.objects.all()
    edit_task = None

    if request.method == 'POST':
        if 'edit_task_id' in request.POST:
            edit_task = get_object_or_404(Task, pk=request.POST['edit_task_id'])
            edit_task.title = request.POST['title']
            edit_task.save()
            return redirect('task_manager')
        else:
            title = request.POST['title']
            Task.objects.create(title=title)
            return redirect('task_manager')
    
    return render(request, 'todo_app/task_manager.html', {'tasks': tasks, 'edit_task': edit_task})

def mark_complete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = True
    task.save()
    return redirect('task_manager')

def edit_task(request, task_id):
    edit_task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        edit_task.title = request.POST['title']
        edit_task.save()
        return redirect('task_manager')

    tasks = Task.objects.all()
    return render(request, 'todo_app/task_manager.html', {'tasks': tasks, 'edit_task': edit_task, 'edit_mode': True})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('task_manager')
