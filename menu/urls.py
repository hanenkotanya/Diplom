from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    path('', views.vse_menu, name='vse_menu'),
    path('one_menu/<int:id>/', views.one_menu, name='one_menu'),
    


]