from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from task.models import Task
# Create your views here.


def home(request):
    print request.user
    return render(request, 'base.html', {})


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'

    def get_queryset(self):
        return Task.objects.filter(hidden=False)


class UserList(ListView):
    model = User
    template_name = 'user_list.html'


class TaskDetail(DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'login'
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('task:task')
    template_name = 'task_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    login_url = '/accounts/login/'
    redirect_field_name = 'login'
    fields = ['title', 'description', 'status', 'hidden']
    success_url = reverse_lazy('task:task')
    template_name = 'task_update.html'


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    login_url = '/accounts/login/'
    redirect_field_name = 'login'
    success_url = reverse_lazy('task:task')
    template_name = 'task_confirm_delete.html'
