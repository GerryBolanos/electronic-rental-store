from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rented', views.rented, name='rented'),
    path('newItem/', views.new_item, name='newItem'),
    path('rentItem/', views.rent_item, name='rentItem'),
    path('removeItem/', views.remove_item, name='removeItem')
]