# Create your views here.

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Task
from .forms import TaskForm
# from django.contrib.auth.decorators import login_required

# @login_required

def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    priority_filter = request.GET.get('priority')
    category_filter = request.GET.get('category')
    status_filter = request.GET.get('status')

    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)
    if category_filter:
        tasks = tasks.filter(category=category_filter)
    if status_filter:
        tasks = tasks.filter(status=status_filter)

        
    return render(request, 'tasks/task_list.html', {'tasks' : tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            print(messages.success(request, 'Task was successfully created.'))
            return redirect('task-list')
    else:
        form = TaskForm()
        print(messages.error)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            print(messages.success(request, 'Task was successfully updated.'))
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)
        print(messages.error)

    return render(request, 'tasks/task_update_form.html', {'form' : form})

def task_delete(request, pk):
    tasks = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        tasks.delete()
        print(messages.success(request, 'Task was successfully deleted.'))
        return redirect('task-list')
    
    return render(request, 'tasks/task_confirm_delete.html', {'task': tasks})
