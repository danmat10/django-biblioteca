from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('/<int:page_number>/', views.index, name='home_paginated'),
    path('busca/', views.search, name='busca'),
    path('busca/<int:page_number>/', views.search, name='busca_paginated'),
    path('detalhes/<int:id>', views.detalhes, name='detalhes'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('editar/<int:id>', views.editar, name='editar'),
]
