__author__ = 'aganiger'

import collections

words = [
    'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
    'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
    'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
    'white', 'orange', "orange", 'red'
]

# Counts how many times key is repeated
word_counts = collections.Counter(words)
print(word_counts)

# you can update the value and it adds up to the existing
word_counts.update({'red': 10})
print(list(word_counts))

print("Print keys of dictionary")
print(word_counts.keys())


# print key and its count
for word in list(word_counts):
    print("%s : %d" % (word, word_counts[word]))

'''Write a Python program to create an instance of an OrderedDict using a given dictionary. Sort the dictionary during the creation and print the members of the dictionary in reverse order'''

print("Original dictionary")
print(word_counts)

orderedDictionary = collections.OrderedDict(word_counts)
for key in orderedDictionary:
    print("%s : %d" % (key, orderedDictionary[key]))

print("\n reverse order")
for key in reversed(orderedDictionary):
    print("%s : %d" % (key, orderedDictionary[key]))





