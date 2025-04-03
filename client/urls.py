from django.urls import path
from . import views


urlpatterns = [
    path('clients/', views.client_list, name = 'client_list'),
    path('client_list_in_json', views.client_list_in_json, name = 'client_list_in_json'),
    path('create_client/', views.client_create, name = 'client_create'),
    path('update/', views.client_update, name = 'client_update'),
    path('delete/', views.client_delete, name = 'client_delete'),
    path('copy/', views.client_copy, name = 'client_copy'),
]