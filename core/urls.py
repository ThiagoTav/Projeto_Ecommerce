# urls.py/core (arquivo principal de configuração de URLs)

from django.contrib import admin
from django.urls import path, include
from project import views as project_views  # Importa as views do projeto com um alias
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from project.views import add_product, buy_product  # Importa funções específicas das views

# Lista de padrões de URLs do projeto
urlpatterns = [
    # URL para a página de administração do Django
    path('admin/', admin.site.urls),
    
    # URL para incluir as URLs definidas no módulo 'project.urls' na rota '/auth/'
    path('auth/', include('project.urls')),
    
    # URL para a página inicial, que redireciona para a página de login
    path('', project_views.home_view, name='login'),
    
    # URL para a página principal do sistema ('home'), que exibe as tarefas
    path('home/', project_views.home_view, name='home'),
    
    # URL para adicionar um novo produto, utilizando a view 'add_product'
    path('add-product/', add_product, name='add-product'),
    
    # URL para comprar um produto específico, usando o ID do produto
    path('buy/<int:product_id>/', buy_product, name='buy-product'),
]