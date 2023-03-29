from django.urls import path, include, re_path
from django.urls import re_path as url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from .models import *

from .views import *

app_name = 'dashboard'

urlpatterns = [
    #path('dashboard',views.dashboard, name='dashboard'),
    path('dashboard', views.dashboard, name="dashboard"),
    #url(r'^relatorio_temperatura', views.relatorio_temperatura, name='relatorio_temperatura'),

    path('relatorio_temperatura/<str:dados_entrada>',
         views.relatorio_temperatura, name="relatorio_temperatura"),
    path('save_data/', views.save_data, name='save_data'),
]
