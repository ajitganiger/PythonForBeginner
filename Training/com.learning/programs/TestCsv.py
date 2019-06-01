__author__ = 'aganiger'

import pandas as pd


data = pd.read_csv("D_DRIVEDownloads\\ml-100k\\u.user", sep="|",
                   names=["User_Id", "Age", "Gender", "Occupation", "Zip_code"])
# print(data.to_string(index=False))  # displays without indexes

print(data.head)
print(data.tail)
print(data.head(3))

print(data[5:15])

# print peticular column
print(data["Gender"].head(3))

column_I_want = ["User_Id", "Gender", "Occupation"]

# print(data[column_I_want].head(10).to_string(index=False))  or use like below
print(data[["User_Id", "Gender", "Occupation"]].head(10).to_string(index=False))

# Conditional data printing
print(data[data.Age > 65])

# male < 35

print(data[(data.Gender == "M") & (data.Age < 20)])

# pm;u prints making User_Id as index
print(data.set_index("User_Id").head(10))

# set_index with inplace replaces
print(data.head(5))
data.set_index("User_Id", inplace=True)
print(data.head(5))

# display with index , choose the rows
print(data.ix[[2, 5, 9]])




