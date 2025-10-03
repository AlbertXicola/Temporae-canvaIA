# filepath: core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('panel/', views.user_panel, name='user_panel'),

]