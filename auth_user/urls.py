from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.signupView, name = 'signup'),
    path('signin', views.signinView, name = 'signin'),
    path('dashboard', views.dashboardView, name = 'dashboard'),
    path('logout', views.logoutView, name = 'logout')
]