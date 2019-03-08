__author__ = 'aganiger'


from collections import Counter

marks = [
    ('Shubham', 89),
    ('Pankaj', 92),
    ('JournalDev', 99),
    ('JournalDev', 99)
]

print(Counter(marks))
print(Counter(marks).most_common(1))
