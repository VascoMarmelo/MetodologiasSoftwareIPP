from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app_index'),
    path('home_page/', views.index, name='home_page'),
    path('perfil/', views.app_perfil, name='app_perfil'),
    path('exemple/', views.app_example, name='app_example'),
    path('', views.playlist_info, name='playlist_info'),
    path('example/', views.app_example, name='app_example'),
    path('perfil/', views.app_profile, name='app_profile')
]