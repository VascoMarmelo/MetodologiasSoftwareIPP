from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.index, name='app_index'),
    path('home_page/', views.index, name='home_page'),
    #path('', views.playlist_info, name='playlist_info'),
    path('example/', views.app_example, name='app_example'),
    path('perfil/', views.app_profile, name='app_profile'),
    path('infopage/', views.infopage, name='infopage'),
    path('infopageArt0/', views.infopageArt0, name='infopageArt0'),
    path('infopageArt1/', views.infopageArt1, name='infopageArt1'),
    path('infopageArt2/', views.infopageArt2, name='infopageArt2'),
    path('infopageplay0/', views.infopageplay0, name='infopageplay0'),
    path('infopageplay1/', views.infopageplay1, name='infopageplay1'),
    path('infopageplay2/', views.infopageplay2, name='infopageplay2'),
    path('infopageplay3/', views.infopageplay3, name='infopageplay3'),
    path('chatboot/', views.chatboot, name='chatboot'),
    path('recommendation/', views.recommendation_view, name='recommendation'),
]