from django.urls import path
from . import views

app_name = 'task' 

urlpatterns = [
    path('create/', views.create_task, name='create'),
    path('edit/<int:task_id>/', views.edit_task, name='edit'),
    path('delete/<int:task_id>/', views.delete_task, name='delete'),
    path('complete/<int:task_id>/', views.complete_task, name='complete'),
    path('', views.task_list, name='list'),  # homepage for tasks
]
