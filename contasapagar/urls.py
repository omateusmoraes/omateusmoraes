
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contasapagar_list, name='contasapagar_list'),
    path('add/', views.add_contasapagar, name='add_contasapagar'),
    path('<int:pk>/edit/', views.edit_contasapagar, name='edit_contasapagar'),
    path('<int:pk>/delete/', views.delete_contasapagar, name='delete_contasapagar'),
]
