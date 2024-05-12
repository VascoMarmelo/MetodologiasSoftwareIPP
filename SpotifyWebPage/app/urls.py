from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app_index'),
    path('perfil', views.app_perfil, name='app_perfil'),
    path('exemplo', views.app_example, name='app_example'),
]