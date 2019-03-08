__author__ = 'aganiger'

'''
The default dictionary can contain duplicate keys.
The advantage of using default dictionary is that we can collect items which belong to the same key'''

from collections import defaultdict

marks = [
    ('Shubham', 89),
    ('Pankaj', 92),
    ('JournalDev', 99),
    ('JournalDev', 98)
]

for key, value in marks:
    print("key: %s, value:%s" % (key, value))

default_dict = defaultdict(list)

for key, value in marks:
    default_dict[key].append(value)

for key in default_dict.keys():
    print("key: %s, value:%s" % (key, default_dict[key]))

