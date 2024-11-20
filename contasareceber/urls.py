from django.urls import path
from . import views

urlpatterns = [
    path('', views.contasareceber_list, name='contasareceber_list'),
    path('add/', views.add_contasareceber, name='add_contasareceber'),
    path('<int:pk>/edit/', views.edit_contasareceber, name='edit_contasareceber'),
    path('<int:pk>/delete/', views.delete_contasareceber, name='delete_contasareceber'),
]
