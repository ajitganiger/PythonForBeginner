__author__ = 'aganiger'

import pandas as pd

# data frames
data = {
    'students': ["Ajit", "Amit", "Rohini", "Akhil"],
    'Maths': [40, 60, 20, 60],
    'Science': [90, 40, 59, 56],
    'Sports': ["BasketBall", "Cricket", "Badminton", "Chess"]
}

students = pd.DataFrame(data, columns=["students", "Sports", "Science", "Maths"])

print(students)

print(students[["students", "Sports"]])