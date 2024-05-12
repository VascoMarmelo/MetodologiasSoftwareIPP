from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, template_name='app/home_page.html')

def app_example(request):
    return render(request, template_name='app/example.html')

def app_perfil(request):
    return render(request, template_name='app/perfil.html')
