__author__ = 'aganiger'

import copy

list = [1, 2, 5, [9, 4], 10]
listDeepCopy = copy.deepcopy(list)

print("List elements before copy")
for i in range(0, len(list)):
    print(list[i], end="\t")

listDeepCopy[3][0] = 430

print("\nDeep Copy List elements after modification of  list")
for i in range(0, len(listDeepCopy)):
    print(listDeepCopy[i], end="\t")

print("\nList elements after copy")
for i in range(0, len(list)):
    print(list[i], end="\t")


listShallowCopy = copy.copy(list)

listShallowCopy[3][0] = 430
print("\nshallow Copy List elements after modification of  list")
for i in range(0, len(listShallowCopy)):
    print(listShallowCopy[i], end="\t")


print("\nList elements after copy")
for i in range(0, len(list)):
    print(list[i], end="\t")
