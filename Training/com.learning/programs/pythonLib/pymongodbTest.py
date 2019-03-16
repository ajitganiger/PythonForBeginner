import pymongo
from pymongo import MongoClient

client = MongoClient()
# client = MongoClient('localhost',27017)
# client = MongoClient('mongodb://localhost:27017')

print(client.list_database_names())

# creating/accessing DB / pytests is the DB name

db = client.pytests
# db = client["pytests"]

# creating a table (collection)
users = db.users

# insert data
user1 = {"name": "Ajit", "password": "mysecurepassword",
         "hobbies": ["cricket", "football"]
         }

user_id = users.insert_one(user1).inserted_id

print(user_id)

userlist = [{"name": "Amit", "password": "test"}, {"name": "Balu", "password": "new"}]

inserted = users.insert_many(userlist)

print(users.find().count())

print(users.find({"name": "Ajit"}).count())

# using condition with $
print(users.find({"hobbies": {"$exists": True}}).count())
