

from django.contrib import admin
from django.contrib.auth import views as views_django
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mi_pagina_inicio, name='inicio'),
    path('login/', views_django.LoginView.as_view(template_name="login.html"), name='login'),
    
]
