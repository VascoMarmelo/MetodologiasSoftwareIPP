from django.shortcuts import render
#from spotipy.oauth2 import SpotifyOAuth


def index(request):
    return render(request, template_name='app/home_page.html')


def app_example(request):
    return render(request, template_name='app/example.html')

def app_profile(request):
    return render(request, 'app/profile_page.html')

def infopage(request):
    return render(request, 'app/infopage.html')

def infopageArt0(request):
    return render(request, 'app/infopageArt0.html')

def infopageArt1(request):
    return render(request, 'app/infopageArt1.html')

def infopageArt2(request):
    return render(request, 'app/infopageArt2.html')

def infopageplay0(request):
    return render(request, 'app/infopageplay0.html')

def infopageplay1(request):
    return render(request, 'app/infopageplay1.html')

def infopageplay2(request):
    return render(request, 'app/infopageplay2.html')

def infopageplay3(request):
    return render(request, 'app/infopageplay3.html')

def infopagelanca0(request):
    return render(request, 'app/infopagelanca0.html')

def infopagelanca1(request):
    return render(request, 'app/infopagelanca1.html')

def infopagelanca2(request):
    return render(request, 'app/infopagelanca2.html')

def infopagelanca3(request):
    return render(request, 'app/infopagelanca3.html')

def chatboot(request):
    return render(request, 'app/chatboot.html')

def recommendation_view(request):
    return render(request, 'app/recommendation.html') 

# Defina suas credenciais do Spotify
#client_id = 'd44f9f4644f34201be982cb94bc66fad'
#client_secret = '999ba5802f5d4edeb0aa97e4907af170'
#redirect_uri = 'http://localhost:8080/callback'  # URL de redirecionamento que você configurou no painel do Spotify

# Inicialize a autenticação do Spotify
#sp = spotipy.Spotify(
#    auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri,
#                              scope='playlist-read-private'))

# Grupo Camoin, Sónia, Lília
#def playlist_info(request):
#    playlists = sp.current_user_playlists()
#    context = {'playlists': []}
#    for playlist in playlists['items']:
#        playlist_info = {
#            'id': playlist['id'],
#            'name': playlist['name'],
#            'total_tracks': playlist['tracks']['total'],
#            'link': playlist['external_urls']['spotify'],
#            'tracks': playlist['tracks'],
#        }

#        context['playlists'].append(playlist_info)

#    return render(request, 'templates/app/playlist.html', context)


#def get_current_track(request):
#    playlists = sp.get_current_tracks()
#    context = {'playlists': []}
#    for playlist in playlists['items']:
#        playlist_info = {
#            'name': playlist['name'],
#            'total_tracks': playlist['tracks']['total'],
#            'link': playlist['external_urls']['spotify']
#        }
#        context['playlists'].append(playlist_info)"""
#    return render(request, 'templates/app/playlist.html', context)