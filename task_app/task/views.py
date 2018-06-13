from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from task.models import Task
# Create your views here.


def home(request):
    return render(request, 'base.html', {})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'


class TaskDetail(DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'create'
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('task')
    template_name = 'task_form.html'
