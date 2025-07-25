"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from to_do.views import TaskListView, create_task, user_register, user_login, user_logout, delete_task, update_task


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TaskListView.as_view(), name='task_list'),
    path('tasks/create/', create_task, name='create_task'),
    path('registration/register/', user_register, name='register'),
    path('registration/login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('tasks/delete/<int:pk>/', delete_task, name='delete_task'),
    path('tasks/update/<int:pk>/', update_task, name='update_task'),
]
