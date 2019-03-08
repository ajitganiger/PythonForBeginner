__author__ = 'aganiger'

import re

import requests


url = "http://dataquestio.github.io/web-scraping-pages/simple.html"

response = requests.get(url)

print(response)
print(response.status_code)
print(response.text)
print(response.content)

from bs4 import BeautifulSoup

data = BeautifulSoup(response.text, "html.parser")
print(data.prettify())

print(list(data.children))

for item in data.children:
    print(type(item))

html = list(data.children)[2]

print(html.title)
print(html.title.text)
print(html.body)

print(list(html.body.children))

body = list(html.body.children)[1]
print(body.get_text())
print(body.text)

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

print(soup.find_all('p', class_='outer-text'))

print(soup.find_all(id="second"))

print("regular experssion")
print(soup.find_all(class_=re.compile("text ")))


print(soup.find_all(text=re.compile(r'First outer paragraph.')))


