__author__ = 'aganiger'


def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print("List value is %s" % list1)
print("List value is %s" % list2)
print("List value is %s" % list3)