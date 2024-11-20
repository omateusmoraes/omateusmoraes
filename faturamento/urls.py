from django.urls import path

from . import views

urlpatterns = [
    path('', views.faturamento_list, name='faturamento_list'),
    path('faturamento/add/', views.faturamento_add, name='faturamento_add'),
    path('<int:pk/edit/', views.faturamento_edit, name='faturamento_edit'),
    path('faturamento/<int:pk>/delete/', views.fatura_delete, name='fatura_delete'),
]

