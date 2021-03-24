"""todoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from core import views
from userauth import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.TaskViewList.as_view(),name='tasks'),
    path('task/<int:pk>',views.TaskDetail.as_view(),name='task'),
    path('task-create/',views.TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>',views.TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>',views.TaskDelete.as_view(),name='task-delete'),
    path('u/',include('userauth.urls'))
]
