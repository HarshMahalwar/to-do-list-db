from django.contrib import admin
from django.urls import path, include

from todo import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name='logout'),
    path('register', views.registerUser, name='register'),
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('github', views.github, name='github'),
    path('linkedin', views.linkedin, name='linkedin'),
    path('about', views.about, name='about'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),
    path('update/<str:pk>', views.updateTask, name='update')
]
