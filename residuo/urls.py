from django.urls import path

from residuo import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('Cadastro_usuario/', views.form_index, name='form_index'),
    path('Cadastro_endereco/', views.form_endereco, name='form_endereco'),
    path('Cadastro_residuo/', views.form_residuo, name='form_residuo'),
    path('Cadastro_categoria/', views.form_categoria, name='form_categoria'),
    path('Cadastro_solicitacao/', views.form_solicitacao, name='form_solicitacao'),
]
