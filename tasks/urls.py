from django.urls import path

from .views import index, TaskListView, TaskDetailView, TaskCreateView

urlpatterns = [
    path('', index, name='index'),
    # path('list', task_list, name='task-list'),
    # path('<ind:id>', task_detail, name='task-detail'),
    path('list/', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('create', TaskCreateView.as_view(), name='task_create'),
]

app_name = 'tasks'