from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.
def index(req):
    diction={}
    if req.method=='POST':
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=e23dd80848c5ec996845fc1863a13704'
        cityname = req.POST.get('cityname')
        response = requests.get(url.format(cityname)).json()
        print(response)



        if response['cod'] == 200:
            city_weather = {
                'city': cityname,
                'temperature': response['main']['temp'],
                'temp_max': response['main']['temp_max'],
                'temp_min': response['main']['temp_min'],
                'feels_like': response['main']['feels_like'],
                'icon': response['weather'][0]['icon'],
                'description': response['weather'][0]['description'],
                'humidity': response['main']['humidity'],
                'wind_speed':response['wind']['speed']

            }


            diction.update({'city_weather': city_weather})
        else:
            err_message = 'City Not Found!!!!'
            diction.update({'err_message': err_message})
    return render(req, 'weather/index.html', context=diction)