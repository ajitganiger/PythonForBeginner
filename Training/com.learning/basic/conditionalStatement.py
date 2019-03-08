check = "Hamburger"

if check == False:
    print("it is False")
elif check == "Hamburger":
    print("ymmmm ,", check)
else:
    print("Nothing matches")

numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

import re;

string = "I AM AJIT small"

new = re.sub("[A-Z]", ":)", string)
print(new)
