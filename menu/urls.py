from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('clientes/', views.clientes, name='clientes'),
    path('contasapagar/', views.contasapagar, name='contasapagar'),
    path('contasareceber/', views.contasareceber, name='contasareceber'),
    path('estoque/', views.estoque, name='estoque'),
    path('faturamento/', views.faturamento, name='faturamento'),
    path('agendamentos/', views.agendamentos, name='agendamentos'),
    path('orcamentos/', views.orcamentos, name='orcamentos'),
]



