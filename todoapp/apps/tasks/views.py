from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import CategoryForm, TaskForm
from .models import Category, Task


def add_category(request):
    template_name = 'tasks/add_category.html'
    context = {}
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()
            messages.success(request, 'Categoria Adicionada com Sucesso')
    form = CategoryForm()
    context['form'] = form
    return render(request, template_name, context)


def list_categories(request):
    template_name = 'tasks/list_categories.html'
    categories = Category.objects.filter(owner=request.user)
    context = {
        'categories': categories
    }
    return render(request, template_name, context)


def edit_category(request, id_category):
    template_name = 'tasks/add_category.html'
    context = {}
    category = get_object_or_404(Category, id=id_category, owner=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('tasks:list_categories')
    form = CategoryForm(instance=category)
    context['form'] = form
    return render(request, template_name, context)


def delete_category(request, id_category):
    category = Category.objects.get(id=id_category)
    if category.owner == request.user:
        category.delete()
    else:
        messages.error(request, 'Você não tem permissão para excluir esta categoria')
        return redirect('core:home')
    return redirect('tasks:list_categories')


def add_task(request):
    template_name = 'tasks/add_task.html'
    context = {}
    if request.method == 'POST':
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()
            form.save_m2m()
            messages.success(request, 'Tarefa Adicionada com Sucesso')
    form = TaskForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)


def list_tasks(request):
    template_name = 'tasks/list_tasks.html'
    context = {}
    tasks = Task.objects.filter(owner=request.user).exclude(status='CD')
    context['tasks'] = tasks
    return render(request, template_name, context)


def edit_task(request, id_task):
    template_name = 'tasks/add_task.html'
    context = {}
    task = get_object_or_404(Task, id=id_task, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, user=request.user, instance=task)
        if form.is_valid:
            form.save()
            return redirect('tasks:list_tasks')
    form = TaskForm(instance=task, user=request.user)
    context['form'] = form
    return render(request, template_name, context)


def delete_task(request, id_task):
    task = Task.objects.get(id=id_task)
    if task.owner == request.user:
        task.delete()
    else:
        messages.error(request, 'Você não tem permissão para excluir esta Tarefa')
        return redirect('core:home')
    return redirect('tasks:list_tasks')
