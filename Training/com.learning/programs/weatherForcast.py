__author__ = 'aganiger'

import requests

city = input("Enter your city: ")

url = "https://www.weather-forecast.com/locations/" + city + "/forecasts/latest"

data=requests.get(url)

print(data)