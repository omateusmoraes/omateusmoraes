from django.urls import path
from . import views

urlpatterns = [
    path('', views.estoque_list, name='estoque_list'),
    path('estoque/add/', views.add_item, name='add_item'),
    path('<int:pk>/edit/', views.edit_item, name='edit_item'),
    path('<int:pk>/delete/', views.delete_item, name='delete_item'),
]
