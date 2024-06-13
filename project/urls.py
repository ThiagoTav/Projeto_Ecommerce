#urls.py/project
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *
from project.views import *

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro_usuario_view, name='cadastro'),
    path('home/', views.home_view, name='home'),
    path('', views.index_view, name='index'),
    path('add-product/', add_product, name='add-product'),
    path('products/', product_list_view, name='product-list'),  # URL para listar produtos
    path('edit-product/<int:pk>/', edit_product, name='edit-product'),
    path('delete-product/<int:pk>/', delete_product, name='delete-product'),
]