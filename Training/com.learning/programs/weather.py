__author__ = 'aganiger'

import re
import urllib.request
from bs4 import BeautifulSoup



def getweatherreport(city):
    try:
        url = "https://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
        response = urllib.request.urlopen(url).read()
        decodedresponse = response.decode("utf-8")

        parseddata = BeautifulSoup(decodedresponse, "html.parser")
        for tag in parseddata.find_all("span", re.compile("read-more-content")):
            print(tag.text)
    except:
        print("City does not exists")

def main():
    city = input("Enter City name: ")
    getweatherreport(city)

# Main start from here
main()