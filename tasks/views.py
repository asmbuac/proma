from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("show_project", id=task.project.id)
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)


@login_required
def list_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "tasks": tasks,
    }
    return render(request, "tasks/list.html", context)

@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return redirect("show_my_tasks")
    context = {
        "task": task,
    }
    return render(request, "tasks/delete.html", context)

@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            project = form.save()
            return redirect("show_project", id=project.project_id)
    else:
        form = TaskForm(instance=task)
    context = {
        "form": form,
    }
    return render(request, "tasks/edit.html", context)
