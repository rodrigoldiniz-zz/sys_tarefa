from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from tasks.models import Task


@login_required(login_url='/contas/login/')
def home(request):
    template_name = 'core/home.html'
    context = {}
    tasks = Task.objects.filter(owner=request.user).filter(end_date=datetime.today())
    context['tasks'] = tasks
    return render(request, template_name, context)
