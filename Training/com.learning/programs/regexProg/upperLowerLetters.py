__author__ = 'aganiger'

'''Python regex to find sequences of one upper case letter followed by lower case letters'''

import re


def uppperLower(string):
    if (re.match(r"[A-Z][a-z]+", string)):
        return True
    else:
        return False


input_string = "Geeks"
print("String %s matches: %s"%(input_string,uppperLower(input_string)))

input_string = "geeekshellono"
print("String %s matches: %s"%(input_string,uppperLower(input_string)))



