from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=dcce203617d8ab4c5e665be3d371b2a5'
    context = None
    
    if(request.method == 'POST'):
        city = request.POST.get('searchLocation').title()
    else:
        city = 'Cape Town'
    
    city_weather = requests.get(url.format(city)).json()

    try:
        weather = {
            'city': city,
            'temperature': str(city_weather['main']['temp'])+' ° C',
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
        }
        context = {'weather': weather}
    except KeyError:
        print("invalid city")
        error = {
            'message': 'Not a valid city'
        }
        weather = {
            'city': 'Not A Valid City',
            'temperature': 'N/A',
            'description': 'N/A',
            'icon': 'N/A',
        }

        context = {'error' : error, 'weather': weather}

    return render(request, 'weather/index.html', context) # returns the index.html template


def about(request):
    return render(request, 'weather/about.html') # returns the index.html template