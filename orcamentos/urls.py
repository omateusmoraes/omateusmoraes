from django.urls import path
from .views import orcamento_list, add_orcamento, edit_orcamento, delete_orcamento

urlpatterns = [
    path('', orcamento_list, name='orcamento_list'),
    path('add/', add_orcamento, name='add_orcamento'),
    path('edit/<int:id>/', edit_orcamento, name='edit_orcamento'),
    path('delete/<int:id>/', delete_orcamento, name='delete_orcamento'),
]
