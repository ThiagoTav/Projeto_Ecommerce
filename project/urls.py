# urls.py/project (arquivo de configuração de URLs específico do aplicativo 'project')

from django.urls import path
from . import views  # Importa as views definidas no mesmo diretório
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *  # Importa todas as views do módulo 'views'
from project.views import *  # Importa todas as views do aplicativo 'project'

# Lista de padrões de URLs específicos do aplicativo 'project'
urlpatterns = [
    # URL para a página de login
    path('login/', views.login_view, name='login'),
    
    # URL para a função de logout
    path('logout/', views.logout_view, name='logout'),
    
    # URL para a página de cadastro de usuário
    path('cadastro/', views.cadastro_usuario_view, name='cadastro'),
    
    # URL para a página inicial (home)
    path('home/', views.home_view, name='home'),
    
    # URL para a página inicial (index)
    path('', views.index_view, name='index'),
    
    # URL para adicionar um novo produto
    path('add-product/', add_product, name='add-product'),
    
    # URL para listar todos os produtos
    path('products/', product_list_view, name='product-list'),
    
    # URL para editar um produto específico (usando seu ID)
    path('edit-product/<int:pk>/', edit_product, name='edit-product'),
    
    # URL para deletar um produto específico (usando seu ID)
    path('delete-product/<int:pk>/', delete_product, name='delete-product'),
]