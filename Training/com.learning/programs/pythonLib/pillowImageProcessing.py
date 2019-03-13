import requests
from io import BytesIO
from PIL import Image

response = requests.get("https://wallpapercave.com/wp/6TQsohO.jpg")

print("Status code:", response.status_code)

image = Image.open(BytesIO(response.content))
#image.now_shows_list = True

print(image.size, image.format, image.mode)
path = "./image." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Error")
