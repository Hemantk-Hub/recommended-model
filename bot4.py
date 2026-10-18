import streamlit as st
import pickle
import joblib

st.title("Movies Recommendation System")

with open("movies.pickle", "rb") as m:
    movies = pickle.load(m)
 
similarity = joblib.load("similarity.joblib")
movie_titles = movies["title"].values

def recommend(name_movie, n=5):
    if name_movie not in movies["title"].values:
        return []

    movie_index = movies[movies["title"] == name_movie].index[0]
    distances = similar[movie_index]

    top = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)[1:n + 1]

    return [movies.iloc[i[0]]["title"] for i in top]

name_movie = st.selectbox("Enter the Movie Name", movie_titles)

if st.button("Recommend"):
    r = recommend(name_movie)
    st.write("The recommended Movies are:")
    for i in r:
        st.write(i)
