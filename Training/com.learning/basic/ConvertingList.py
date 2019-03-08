__author__ = 'aganiger'

weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sun', 'mon', 'mon']

print("Below is the list")
for i in range(0, len(weekdays)):
    print(weekdays[i], end = '')

print(end="\n");

listAsSet = set(weekdays)
print("List to set %s" % listAsSet)

listAsTuple = tuple(weekdays)
print("List as tuple " + str(listAsTuple))

listAsString = ' '.join(weekdays)
print("List as String :" + listAsString)

# print number of occurance of an element

print("mon found %s times " % weekdays.count("mon"))

for i in range(0, len(set(weekdays))):
    day = weekdays[i]
    count = str(weekdays.count(day))
    print(day + " found " + count + " times ")

# this is new text added by progress
