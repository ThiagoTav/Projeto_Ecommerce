#urls.py/core
from django import views
from django.contrib import admin
from django.urls import path, include
from project import views as project_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from project.views import add_product, buy_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('project.urls')),
    path('', project_views.home_view, name='login'),
    path('home/', project_views.home_view, name='home'),
    path('add-product/', add_product, name='add-product'),
    path('buy/<int:product_id>/', buy_product, name='buy-product'),
]