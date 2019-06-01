__author__ = 'aganiger'

import os

print(os.path.expanduser('~'))
# print(os.path.isfile("D_DRIVEAppData\\Local\\Programs\\Python\\Python36-32\\python.exe"))


# validate Email address

import re


def isEmail(email_id):
    print(re.search(".*", email_id))
    if re.match(".*@*[\.com|\.co\.in]$", email_id) != None:
        return True
    return False


print(isEmail("testo@q.com"))

# What is the output of below
list = ['a', 'b', 'c', 'd', 'e']
print(list[10:])