from django.urls import path
from . import views

urlpatterns = [
    path('edit/<int:record_id>/', views.edit_single_record, name='edit_record'),
    path('', views.home, name='home'),
    path('add/', views.add_injection, name='add_injection'),
    path('records/', views.records_list, name='records_list'),
    path('edit/', views.edit_records, name='edit_records'),

]
