"""sistemaweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inicio.views import index

urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),

    # include para acessar a minha app inicio
    path('inicio/', include('inicio.urls')),
    path('clientes/', include('clientes.urls')),
    path('estoque/', include('estoque.urls')),
    path('faturamento/', include('faturamento.urls')),
    path('agendamentos/', include('agendamentos.urls')),
    path('login/', include('login.urls')),
    path('menu/', include('menu.urls')),
    path('contasapagar/', include('contasapagar.urls')),
    path('contasareceber/', include('contasareceber.urls')),
    path('orcamentos/', include('orcamentos.urls')),




]
