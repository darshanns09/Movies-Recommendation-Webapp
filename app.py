import pandas as pd
import streamlit as st
import pickle
import requests

def fetchposter(movies_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=cdac48738decbc2db08cff3774e36e66'.format(movies_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/original/' +  data['poster_path']




def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity_matrix[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movie = []
    recommend_movie_poster = []
    for i in movies_list:
        movies_id = movies.iloc[i[0]].movie_id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_movie_poster.append(fetchposter(movies_id))
    return recommend_movie,recommend_movie_poster

similarity_matrix = pickle.load(open('Similarity.pkl','rb'))

movies_dict = pickle.load(open('Movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)




st.title('Movie Recommendation System')

selected_movies = st.selectbox(
    'select Movies Name',
     movies['title'].values)

if st.button('Recommendation'):
    names,posters = recommend(selected_movies)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])