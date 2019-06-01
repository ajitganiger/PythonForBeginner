__author__ = 'aganiger'

import pandas as pd
import numpy as np

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
print(lens.head())

# most_rated=lens.groupby("title").size().order(ascending=False)[:20]
# print(most_rated)

print(lens.title.value_counts()[:20])

movie_stat = lens.groupby("title").agg({"rating": [np.size, np.mean]})
print(movie_stat.head())

print(movie_stat.sort_values([("rating", "size")], ascending=False).head())