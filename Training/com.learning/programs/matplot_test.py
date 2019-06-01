__author__ = 'aganiger'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

headers = ["user_id", "movie_id", "rating", "unix_timestamp"]
ratings = pd.read_csv("D_DRIVEDownloads\\ml-100k\\u.data", sep="\t", names=headers)
print(ratings.head())

headers2 = ["movie_id", "title", "release_date", "video_release_data", "ibdb_url"]
movies = pd.read_csv("D_DRIVEDownloads\\ml-100k\\u.item", sep="|", names=headers2,
                     usecols=range(5), encoding="ISO-8859-1")
print(movies.head())

movie_rating = pd.merge(movies, ratings)

print(movie_rating.head())

user_headers = ["user_id", "age", "gender", "occupation", "zip_code"]
users = pd.read_csv("D_DRIVEDownloads\\ml-100k\\u.user", sep="|", names=user_headers)
print(users.head())

lens = pd.merge(movie_rating, users)

users.age.hist(bins=30)
plt.title("Distribution of users Age")
plt.xlabel("Age")
plt.ylabel("count of users")
#plt.show()

most_50=lens.movie_id.value_counts().sort_values(ascending=False)
print(most_50.head())

