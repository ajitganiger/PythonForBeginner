from bs4 import BeautifulSoup
import requests
import re

params = {"q": "pizza"}

r = requests.get("http://google.com/search", params=params)
print("Status:", r.status_code)
print("URL: ", r.url)

soup = BeautifulSoup(r.content, "html.parser")
# print(soup.prettify())

# print(list(soup.children))

html = list(soup.children)[1]
print(html.title)

divtags = soup.findAll('div', role='heading')
for tag in divtags:
    print(tag.find('span').text)
