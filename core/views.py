from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from core.forms import TaskCreationForm
from .models import Task
from django.views.decorators.cache import cache_control




#Create your views here.


def landing_page(request):
    return render(request,'core/landing_page.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='users:login')
def home(request):
    form = TaskCreationForm()
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('core:home')


    tasks = Task.objects.filter(user=request.user)


    context = {'form': form, 'tasks':tasks}
    return render(request, 'core/index.html', context)


@login_required(login_url='users:login')
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        formedit = TaskCreationForm(request.POST, instance=task)
        if formedit.is_valid():
            formedit.save()
            return redirect('core:home')
    else:
        formedit = TaskCreationForm(instance=task)
    context = {'formedit': formedit, 'task':task} 
    return render(request, 'core/edit_task.html', context)


@login_required(login_url='users:login')
def detele_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('core:home')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='users:login')
def calendar(request):
    tasks = Task.objects.filter(user=request.user)
    context = {'tasks':tasks} 
    return render(request, 'core/calendar.html', context)




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_view(request):
    logout(request)
    return redirect('users:login')


