from django.urls import path
from . import views
urlpatterns = [
    path('assets/', views.asset_list, name = 'asset_list'),
    path('create_asset/', views.asset_create, name = 'asset_create'),
]