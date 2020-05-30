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
        form = TaskForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()
            form.save_m2m()
            messages.success(request, 'Tarefa Adicionada com Sucesso')
    form = TaskForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)


def tasks_list(request):
    template_name = 'tasks/tasks_list.html'
    context = {}
    tasks = Task.objects.filter(owner=request.user).exclude(status='CD')
    context['tasks'] = tasks
    return render(request, template_name, context)
