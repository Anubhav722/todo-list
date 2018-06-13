from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from task.models import Task
# Create your views here.


def home(request):
    print request.user
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
            return redirect('task:home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'

    def get_queryset(self):
        return Task.objects.filter(hidden=False)


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
