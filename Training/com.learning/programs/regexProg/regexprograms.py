__author__ = 'aganiger'

# Program that matches a word containing g followed by one or more es using regex

import re



def matchword(string):
    output = re.findall(r"[g][e]+\w*", string)
    if output:
        print(*output)
    else:
        print("no match found")


string = "geeks for geeks"
matchword(string)
string = "graphic era"
matchword(string)

'''Program to check if a string contains any special character'''


def isContainsSpecialChar(string):
    output = re.findall(r"[^a-zA-Z0-9\s]+", string)
    print(output)
    if output:
        print("Contains Special char")
    else:
        print("does not contains special char")


string = "Geeks$For$Geeks"
isContainsSpecialChar(string)
string = "Geeks For Geeks"
isContainsSpecialChar(string)

'''program to extract Email-id from URL text file'''


def extractEmail(string):
    output = re.findall(r"[\w\.-]+@[\w\.]+", string)
    print(output)


string = '''Hello
This is Geeksforgeeks
review-team@geeksforgeeks.org
contribute@geeksforgeeks.org
GfG is a portal for geeks
feedback@geeksforgeeks.org
careers@geeksforgeeks.org
ajit.smile4u@gmail.com'''
extractEmail(string)

string = "ello shubhamg199630@gmail.com Rohit neeraj@gmail.com"
extractEmail(string)

'''Remove leading zeros from an IP address'''


def removeLeadingZero(string):
    output = re.sub(r"\b0+(\d)", r"\1", string)
    print(output)


string = "100.020.003.400"
print("Original string", string)
removeLeadingZero(string)


def findurls(string):
    # output=re.findall(r"http[s]://[a-zA-Z0-9.\/\s]+",string)
    output = re.findall(r"http[s]?://[^\s]+", string)
    print(output)


string = '''My Profile:
https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles
in the portal of http://www.geeksforgeeks.org/'''

findurls(string)