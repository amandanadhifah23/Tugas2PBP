from django.shortcuts import render
from todolist.models import Task
# Registrasi
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Login
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Logout
from django.contrib.auth import logout
# Menambahkan cookies
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import FormTask

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data = Task.objects.filter(user=request.user)
    context = {
    'list_todo': data,
    'username':  request.user.username,
    }
    return render(request, "todolist.html", context)

# Registrasi
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

# Page create task
def create_task(request):
    form = FormTask()

    if request.method == "POST":
        form = FormTask(request.POST)
        if form.is_valid():
            form = Task()
            form.user = request.user
            form.date = datetime.datetime.now()
            form.title = request.POST.get('title')
            form.description = request.POST.get('description')
            form.save()
            return redirect('todolist:show_todolist')
    else:
        form = FormTask()

    context = {'form': form}
    return render(request, 'create_task.html', context)


# Login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# Logout
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


