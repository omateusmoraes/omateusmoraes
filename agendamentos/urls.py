from django.urls import path
from . import views

urlpatterns = [
    path('', views.agendamento_list, name='agendamento_list'),
    path('add/', views.add_agendamento, name='add_agendamento'),
    path('<int:pk>/edit/', views.edit_agendamento, name='edit_agendamento'),
    path('<int:pk>/delete/', views.delete_agendamento, name='delete_agendamento'),
]
