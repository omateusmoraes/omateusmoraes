
from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes_list, name='clientes_list'),
    path('add/', views.add_client, name='add_client'),
    path('<int:pk>/edit/', views.edit_client, name='edit_client'),
    path('<int:pk>/delete/', views.delete_client, name='delete_client'),
]
