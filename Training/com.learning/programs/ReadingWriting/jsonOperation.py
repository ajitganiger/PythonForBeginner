import json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    oldfile = open("./ages.json", "r+")
    data = json.loads(oldfile.read())
    print("Current age is ", data["age"], "-- Adding a year")
    data["age"] = data["age"] + 1
    print("new age is", data["age"])
else:
    oldfile = open("./ages.json", "w+")
    data = {"name": "Ajit", "age": 28}
    print("No file found , setting default values to ", data)

oldfile.seek(0)
oldfile.write(json.dumps(data))
oldfile.close()
