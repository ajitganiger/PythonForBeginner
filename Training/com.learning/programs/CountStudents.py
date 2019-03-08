__author__ = 'aganiger'

import collections

classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)

# print classwise roll numbers
roll_num = collections.defaultdict(list)
for k, v in classes:
    roll_num[k].append(v)

print(roll_num.items())

# Count number of students in each class
for clas in roll_num.keys():
    print("%s has %d students" % (clas, len(roll_num.get(clas))))

# or yon do below too
students = collections.Counter(classname for classname, student in classes)
print(students)