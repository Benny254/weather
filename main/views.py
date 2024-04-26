from django.shortcuts import render
import requests
from .models import cities

def weather_app(request):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    weather_data = []

    cities_list = cities.objects.all()
    for city in cities_list:
        get_weather = requests.get(url.format(city)).json()

        print(get_weather)

    return render(request, 'weather/weather_page.html', {'weather_data': weather_data})
