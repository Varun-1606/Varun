import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample data: User ratings for movies
data = {
    'User': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C', 'D', 'D'],
    'Movie': ['Avengers', 'Titanic', 'Inception', 'Avengers', 'Inception', 'Titanic', 'Inception', 'Matrix', 'Matrix', 'Avengers'],
    'Rating': [5, 4, 3, 5, 4, 4, 5, 5, 4, 3]
}
df = pd.DataFrame(data)

# Pivot table to create a user-item matrix
user_movie_matrix = df.pivot_table(index='User', columns='Movie', values='Rating').fillna(0)

# Calculate cosine similarity between users
user_similarity = cosine_similarity(user_movie_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

# Recommend movies based on similar users
def recommend_movies(user):
    if user not in user_similarity_df.index:
        return "User not found."

    similar_users = user_similarity_df[user].sort_values(ascending=False).index[1:3]
    recommendations = []

    for u in similar_users:
        movies_watched_by_u = user_movie_matrix.loc[u]
        recommended_movies = movies_watched_by_u[movies_watched_by_u > 0].index.tolist()
        recommendations.extend(recommended_movies)
    
    # Remove duplicates and movies already watched by the user
    watched_movies = user_movie_matrix.loc[user][user_movie_matrix.loc[user] > 0].index
    final_recommendations = list(set(recommendations) - set(watched_movies))

    return final_recommendations if final_recommendations else "No new recommendations available."

# Example usage
user_input = 'A'
print(f"Recommended movies for User {user_input}: {recommend_movies(user_input)}")
