from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Task

# Create your views here.


def index(request):
    return render(request, 'index.html', {'name': 'World'})


class TaskDetailView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    model = Task
    template_name = "task_detail.html"


class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"

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
