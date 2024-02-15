import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

user_ratings_df = pd.read_csv("../input/the-movies-dataset/ratings.csv")
user_ratings_df.head()
movie_metadata = pd.read_csv("../input/the-movies-dataset/movies_metadata.csv")
movie_metadata = movie_names[['title', 'genres']]
movie_metadata.head()

movie_data = user_ratings_df.merge(movie_metadata, on='movieId')
movie_data.head()


user_item_matrix = ratings_data.pivot(index=['userId'], columns=['movieId'], values='rating').fillna(0)
user_item_matrix


cf_knn_model= NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=10, n_jobs=-1)
cf_knn_model.fit(user_item_matrix)


#THE FOLLOWING METHOD IS USED TO RECOMMEND A MOVIE ACCORDING TO "collaborative filtering".
def movie_recom(movie_name, matrix, cf_model, n_recs):

    cf_knn_model.fit(matrix)
    movie_id = process.extractOne(movie_name, movie_names['title'])[2]
    distances, indices = cf_model.kneighbors(matrix[movie_id], n_neighbors=n_recs)
    movie_rec_ids = sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1]
    cf_recs = []
    for i in movie_rec_ids:
        cf_recs.append({'Title':movie_names['title'][i[0]],'Distance':i[1]})
    df = pd.DataFrame(cf_recs, index = range(1,n_recs))
    return df
# n denotes number of movies recommended.
n= 10
mn=input("ENTER MOVIE NAME")
movie_recom('Batman', user_rating_matrix, cf_knn_model, n) 
