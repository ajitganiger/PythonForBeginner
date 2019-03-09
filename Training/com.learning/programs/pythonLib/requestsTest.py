import requests

params = {"q": "pizza"}


def writeData(data):
    file = open("./page.html", "w+")
    file.write(data)
    file.close()


r = requests.get("http://google.com/search", params=params)
print("Status:", r.status_code)
print("URL: ", r.url)
print("Writing response data to file ./page.html")
writeData(r.text)

# post requests

url = "https://www.w3schools.com/php/welcome.php"
data = {"name": "Ajit", "email": "ajit@test.com"}
r = requests.post(url, data)

print("code ", r.status_code)
print(r.text)
