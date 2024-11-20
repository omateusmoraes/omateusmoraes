from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),  # Atualizando para usar user_login
    path('menu/', views.menu, name='menu'),
    # Outras rotas
]
