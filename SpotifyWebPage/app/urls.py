from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.index, name='app_index'),
    path('home_page/', views.index, name='home_page'),        
    #path('', views.playlist_info, name='playlist_info'),
    path('example/', views.app_example, name='app_example'),    
    path('perfil/', views.app_profile, name='app_profile'),
    path('recommendation/', views.recommendation_view, name='recommendation'),
    path('artist/', views.app_artist, name='app_artist'),
    path('track/', views.app_track, name='app_track'),
]