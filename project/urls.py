#urls.py/project
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro_usuario_view, name='cadastro'),
    path('home/', views.home_view, name='home'),
    path('', views.index_view, name='index'),
]