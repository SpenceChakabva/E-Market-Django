from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'app'
urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.login, name='login'),
    path('panel', views.panel, name='panel')
]