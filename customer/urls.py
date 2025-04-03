from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name = 'customer_list'),
    path('customer-create/', views.customer_create, name = 'customer_create'),
]
