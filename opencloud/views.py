from shutil import ExecError
from ssl import HAS_TLSv1_2
from django.shortcuts import render
import json 
import requests

def home(request):
    if request.method == "POST":
        city = request.POST.get("cityname", False)
        api_key = "your api"
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")

        try:
            data = json.loads(response.text)

        except Exception as e:
            data = "Error..."

        context = {
            "wind_speed" : data["wind"]["speed"],
            "humidity" : data["main"]["humidity"],
            "cloud":data["weather"][0]["main"],  
            "city":city, 
            "icon":data["weather"][0]["icon"],
            "description":data["weather"][0]["description"],
            "temperature":int(float(data["main"]["temp"]) - 275.15),
            "country_name": data["sys"]["country"],
            "feels": int(float(data["main"]["feels_like"]) - 275.15) ,
        }
      
        return render(request, "home.html", context)
    else:
        return render(request, "home.html")



