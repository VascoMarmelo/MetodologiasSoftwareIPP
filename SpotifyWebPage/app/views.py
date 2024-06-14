from django.shortcuts import render


def index(request):
    return render(request, template_name='app/home_page.html')


def app_example(request):
    return render(request, template_name='app/example.html')


def app_profile(request):
    return render(request, 'app/profile_page.html')


def app_artist(request, id):    
    return render(request, 'app/artist_page.html', {'artist_id': id})


def app_track(request, id):
    return render(request, 'app/track_page.html', {'track_id': id})


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


def recommendation_view(request):
    return render(request, 'app/recommendation.html') 


def chatboot(request):
    return render(request, 'app/chatboot.html')

