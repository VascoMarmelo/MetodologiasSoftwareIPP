from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app_index'),
    path('home_page/', views.index, name='home_page'),
    path('example/', views.app_example, name='app_example'),
    path('perfil/', views.app_profile, name='app_profile')
]