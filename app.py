import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "http://api.themoviedb.org/3/movie/{}?api_key=6a82693df1c55957a51c70805a584c18#".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "http://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

def recommend(movie):
    movie_idx = movies[movies['title']==movie].index[0]
    similarities = similarity[movie_idx]
    movie_list = sorted( list(enumerate(similarities)) , reverse= True ,key=lambda x : x[1])[1:14]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
                # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies , recommended_movies_posters

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
        "Type or select a movie from the options",
        movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    col1 , col2 , col3  = st.columns(3)
    col4 , col5 , col6  = st.columns(3)
    col7 , col8 , col9 = st.columns(3)
    col10 , col11 , col12 = st.columns(3)
    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.header(names[1])
        st.image(posters[1])
    with col3:
        st.header(names[2])
        st.image(posters[2])
    with col4:
        st.header(names[3])
        st.image(posters[3])
    with col5:
        st.header(names[4])
        st.image(posters[4])
    with col6:
        st.header(names[5])
        st.image(posters[5])
    with col7:
        st.header(names[6])
        st.image(posters[6])
    with col8:
        st.header(names[7])
        st.image(posters[7])
    with col9:
        st.header(names[8])
        st.image(posters[8])
    with col10:
        st.header(names[9])
        st.image(posters[9])
    with col11:
        st.header(names[10])
        st.image(posters[10])
    with col12:
        st.header(names[11])
        st.image(posters[11])
