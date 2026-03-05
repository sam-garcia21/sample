from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import CreateView, DeleteView

from .forms import TaskForm
from .models import Task, TaskGroup

# Create your views here.


def index(request):
    return render(request, 'index.html', {'name': 'World'})


class TaskDetailView(DetailView):
    # login_url = '/accounts/login/'
    model = Task
    template_name = "task_detail.html"
    form_class = TaskForm


class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['taskgroups'] = TaskGroup.objects.all()
        context['form'] = TaskForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request, *args, **kwargs)
        # t = Task()
        # t.name = request.POST.get('name')
        # t.due_date = request.POST.get('due_date')
        # t.taskgroup = TaskGroup.objects.get(pk=request.POST.get('taskgroup'))
        # t.save()
        # return self.get(request, *args, **kwargs)
    
class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_detail.html'
    form_class = TaskForm
        

        

# class TaskListView(TemplateView):
#     template_name = "task_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['tasks'] = tasks
#         return context

#     def post(self, request, *args, **kwargs):
#         print(request.POST.get('task_name'))
#         tasks.append(request.post.get('task_name'))
#         context = self.get_context_data(**kwargs)
#         return self.get(request, *args, **kwargs)
