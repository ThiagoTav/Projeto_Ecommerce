#urls.py/core
from django.contrib import admin
from django.urls import path, include
from project import views as project_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('project.urls')),
    path('', project_views.home_view, name='home'),
]