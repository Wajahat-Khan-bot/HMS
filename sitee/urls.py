from django.urls import path
from . import views

urlpatterns = [
    path('sitee/', views.sitee_list, name= 'sitee_list'),
    path('sitee-create/', views.sitee_create, name = 'sitee_create')
]
