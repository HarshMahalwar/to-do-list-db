from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from .models import task
from .forms import taskForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exists")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username or password is invalid.')
    context = {'page': page}
    return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    page = 'register'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "The user already exists.")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "The password is incorrect.")
            return redirect('register')
    context = {'page': page}
    return render(request, 'register.html', context)


def home(request):
    t = task.objects.all()
    context = {'tasks': t}
    return render(request, 'home.html', context)


@login_required(login_url='login')
def add(request):
    t = taskForm()
    if request.method == 'POST':
        fr = taskForm(request.POST)
        if fr.is_valid():
            fr.save()
            return redirect('home')
    context = {'tasks': t}
    return render(request, 'task_form.html', context)


def deleteTask(request, pk):
    r = task.objects.get(id=pk)
    if request.user != r.host:
        return HttpResponse("You don't have the permission to remove this task from the list.")
    if request.method == 'POST':
        r.delete()
        return redirect('/')
    context = {'task': r}
    return render(request, 'delete.html', context)


def linkedin(request):
    return redirect('https://www.linkedin.com/in/harsh-mahalwar-4310b316a/')


def github(request):
    return redirect('https://github.com/HarshMahalwar?tab=repositories')


def updateTask(request, pk):
    r = task.objects.get(id=pk)
    fr = taskForm(instance=r)
    if request.user != r.host:
        return HttpResponse("You don't have the permission to remove this task from the list.")
    if request.method == 'POST':
        fr = taskForm(request.POST, instance=r)
        if fr.is_valid():
            fr.save()
            return redirect('/')
    context = {'tasks': fr}
    return render(request, 'update_page.html', context)


def about(request):
    return redirect('/')