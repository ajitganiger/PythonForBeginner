__author__ = 'aganiger'

import re
from collections import Counter


def mostCommontNumber(word):
    #below line finds all the numbers in a given string
    numbers = re.findall(r'\d+', word)
    print(numbers)
    counts = Counter(numbers)
    print(counts)
    print(counts.most_common(1))
    max=0
    max_ele=0
    for key in counts.keys():
        if counts[key]>max:
            max=counts[key]
            max_ele=key

    return max_ele

string = "geek55of55geeks4abc3dr2"

print(mostCommontNumber(string))