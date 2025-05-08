from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_injection, name='add_injection'),
    path('add/', views.add_injection, name='add_injection'),
]
