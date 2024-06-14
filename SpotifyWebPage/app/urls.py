from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.index, name='app_index'),
    path('home_page/', views.index, name='home_page'),        
    
    path('example/', views.app_example, name='app_example'),    
    path('perfil/', views.app_profile, name='app_profile'),
    
    path('artist/<str:id>/', views.app_artist, name='app_artist'),
    path('track/<str:id>/', views.app_track, name='app_track'),
    path('recommendation/', views.recommendation_view, name='recommendation'),

    path('chatboot/', views.chatboot, name='chatboot'),

    path('infopageplay0/', views.infopageplay0, name='infopageplay0'),
    path('infopageplay1/', views.infopageplay1, name='infopageplay1'),
    path('infopageplay2/', views.infopageplay2, name='infopageplay2'),
    path('infopageplay3/', views.infopageplay3, name='infopageplay3'),

    path('infopagelanca0/', views.infopagelanca0, name='infopagelanca0'),
    path('infopagelanca1/', views.infopagelanca1, name='infopagelanca1'),
    path('infopagelanca2/', views.infopagelanca2, name='infopagelanca2'),
    path('infopagelanca3/', views.infopagelanca3, name='infopagelanca3'), 
]