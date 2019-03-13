from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

search = input("search for:")
params = {"q": search}

r = requests.get("http://www.bing.come/images/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
links = soup.findAll("a", {"class": "thumb"})

for item in links:
    img_obj = requests.get(item.attr["href"])
    title = item.attr["href"].split("/")[-1]
    img = Image.open(BytesIO(img_obj.content))
    img.save("./images/" + title, img.format)


# dir_name = search.replace(" ","_").lower()
# if not os.path.isdir(dir_name):
#     os.makedirs(dir_name)d


