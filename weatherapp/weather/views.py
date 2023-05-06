from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=dcce203617d8ab4c5e665be3d371b2a5'

    city = 'Cape Town'

    city_weather = requests.get(url.format(city)).json()

    print(city_weather)

    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    context = {'weather': weather}

    return render(request, 'weather/index.html', context) # returns the index.html template


def about(request):
    return HttpResponse('<h1>Welcome to the about page<h1>')