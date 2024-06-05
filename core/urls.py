#urls.py/core
from django.contrib import admin
from django.urls import path, include
from project import views as project_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('project.urls')),
    path('', project_views.home_view, name='login'),
    path('home/', project_views.home_view, name='home'),

]