__author__ = 'aganiger'

import datetime

print("Current date and time: ", datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

for i in range(0, 4):
    day = datetime.date.today()
    print("day", today + datetime.timedelta(days=i))
    i = i + 1;

print('Yesterday : ', yesterday)
print('Today : ', today)
print('Tomorrow : ', tomorrow)


##check if its leap Year

def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False


print(isLeapYear(2004))