__author__ = 'aganiger'

import requests

url = 'https://api.github.com/user'
username = "ajit.smile4u@gmail.com"
password = "Rock1234"


def getUserDetails(username, password):
    response = requests.get(url, auth=(username, password))
    print(response.status_code)
    print(response.text)


def passingParameters(reponame):
    payload = {"name": reponame}
    response = requests.get("https://api.github.com/user/repos", params=payload, auth=(username, password))
    print(response.url)
    print(response.json())


def getRepos(session):
    response = session.get(url)
    print("Requests session handling")
    print(response.json())


def main():
    getUserDetails(username, password)
    passingParameters("frozenStrawberry")

    session = requests.session()
    session.auth = (username, password)
    session.headers.update({"Accept": "application/json"})
    session.params = {"name", "frozenStrawberry"}
    getRepos(session)


main()