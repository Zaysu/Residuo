from django.urls import path

from residuo import views, view_listar_dados

urlpatterns = [
    path('home/', views.index, name='index'),
    path('Cadastro_usuario/', views.form_index, name='form_index'),
    path('Cadastro_endereco/', views.form_endereco, name='form_endereco'),
    path('Cadastro_residuo/', views.form_residuo, name='form_residuo'),
    path('Cadastro_categoria/', views.form_categoria, name='form_categoria'),
    path('Cadastro_solicitacao/', views.form_solicitacao, name='form_solicitacao'),
    path('listar_pessoa/', view_listar_dados.listar_pessoa, name='listar_pessoa'),
    path('listar_endereco/', view_listar_dados.listar_endereco, name='listar_endereco'),
    path('listar_residuo/', view_listar_dados.listar_residuo, name='listar_residuo'),
    path('listar_solicitacao/', view_listar_dados.listar_solicitacao, name='listar_solicitacao'),
    path('listar_categoria/', view_listar_dados.listar_categoria, name='listar_categoria'),
    
    path('login/', views.form_login, name='login'),
    path('forgot/', views.views_recuperar_senha, name='recuperar_senha'),
    path('logout/', views.Logout, name='logout'),

]
